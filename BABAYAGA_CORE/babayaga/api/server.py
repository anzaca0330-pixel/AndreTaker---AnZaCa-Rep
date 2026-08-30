import os
import shutil
from datetime import datetime, timezone
from fastapi import FastAPI, UploadFile, File, Form, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

# Importación relativa y segura de la arquitectura de dos núcleos
from ..core.forensics.xref import XrefAnalyzer
from ..core.forensics.raster import RasterAnalyzer
from ..core.custody import CustodyTracker
from ..core.intelligence.mitigation import AntiPalantir
from ..core.intelligence.network import NetworkAuditor
from . import database

# Inicializar Base de Datos
database.init_db()

app = FastAPI(
    title="AndreTaker — BabaYaga Core API",
    description="API interna offline para auditoría forense electoral y autodefensa de red.",
    version="2.0"
)

# Permitir conexiones CORS para la interfaz web local
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Estructuras de datos
class AnalizarRequest(BaseModel):
    evidencia_id: int

class APRequest(BaseModel):
    evidencia_id: int

@app.get("/api/casos")
def listar_casos():
    conn = database.get_connection()
    casos = conn.execute("SELECT * FROM casos").fetchall()
    conn.close()
    return [dict(c) for c in casos]

@app.get("/api/casos/{caso_id}/resumen")
def obtener_resumen_caso(caso_id: int):
    resumen = database.obtener_resumen_caso(caso_id)
    if not resumen:
        raise HTTPException(status_code=404, detail="Caso no encontrado")
    return resumen

@app.get("/api/evidencias")
def listar_evidencias(caso_id: int = 1):
    conn = database.get_connection()
    evidencias = conn.execute(
        "SELECT e.*, r.discrepancia_xref, r.varianza_cero_detectada, r.score_vectorial "
        "FROM evidencias e LEFT JOIN analisis_resultados r ON e.id = r.evidencia_id "
        "WHERE e.caso_id = ?", (caso_id,)
    ).fetchall()
    conn.close()
    return [dict(e) for e in evidencias]

@app.get("/api/network/status")
def obtener_estado_red():
    """Devuelve la comprobación de seguridad de red (interfaces VPN y puertos escuchando)."""
    vpn_status = NetworkAuditor.detect_active_vpn()
    ports = NetworkAuditor.audit_listening_ports()
    return {
        "vpn": vpn_status,
        "listening_ports": ports,
        "is_safe": vpn_status.get("vpn_active", False) and len(ports) == 0
    }

@app.post("/api/evidencia/upload")
async def cargar_evidencia(caso_id: int = Form(1), file: UploadFile = File(...)):
    """Guarda el archivo localmente y lo registra en la base de datos de custodia."""
    upload_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../00_MUESTRAS_EVIDENCIA/CARGADAS"))
    os.makedirs(upload_dir, exist_ok=True)
    
    file_path = os.path.join(upload_dir, file.filename)
    
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
        
    sha256_orig = CustodyTracker.calcular_sha256(file_path)
    fecha_utc = datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
    
    conn = database.get_connection()
    try:
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO evidencias (caso_id, nombre_archivo, ruta_absoluta, sha256_original, fecha_registro) "
            "VALUES (?, ?, ?, ?, ?)",
            (caso_id, file.filename, file_path, sha256_orig, fecha_utc)
        )
        conn.commit()
        ev_id = cursor.lastrowid
        database.registrar_custody_log(ev_id, "UPLOAD_API", f"Archivo recibido vía API web. SHA-256: {sha256_orig}")
        return {"status": "success", "evidencia_id": ev_id, "sha256": sha256_orig, "ruta": file_path}
    except Exception as e:
        conn.close()
        raise HTTPException(status_code=400, detail=f"Error al registrar evidencia: {str(e)}")
    finally:
        conn.close()

@app.post("/api/evidencia/analizar")
def analizar_evidencia(req: AnalizarRequest):
    """Ejecuta el escaneo pericial multicapas de BabaYaga."""
    conn = database.get_connection()
    evidencia = conn.execute("SELECT * FROM evidencias WHERE id = ?", (req.evidencia_id,)).fetchone()
    if not evidencia:
        conn.close()
        raise HTTPException(status_code=404, detail="Evidencia no encontrada")
        
    ruta = evidencia["ruta_absoluta"]
    
    # Invocación de los módulos del núcleo
    xref_res = XrefAnalyzer.analizar_estructura(ruta)
    raster_res = RasterAnalyzer.analizar_imagenes(ruta)
    vec_res = RasterAnalyzer.detectar_elementos_vectoriales(ruta)
    
    has_variance_zero = False
    imgs = raster_res.get("imagenes", [])
    if isinstance(imgs, list):
        has_variance_zero = any(i.get("varianza_cero", False) for i in imgs)
        
    fecha_utc = datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
    
    cursor = conn.cursor()
    try:
        cursor.execute(
            "INSERT OR REPLACE INTO analisis_resultados "
            "(evidencia_id, exit_code, discrepancia_xref, xref_detalle, cant_imagenes, "
            " varianza_cero_detectada, contiene_vectores, score_vectorial, fecha_analisis) "
            "VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
            (
                req.evidencia_id,
                xref_res.get("exit_code"),
                xref_res.get("XREF_discrepancia"),
                xref_res.get("detalle")[:500],
                len(imgs),
                has_variance_zero,
                vec_res.get("contiene_vectores"),
                vec_res.get("score_vectorial"),
                fecha_utc
            )
        )
        conn.commit()
        database.registrar_custody_log(req.evidencia_id, "ANALYZE_API", "Análisis pericial completado mediante API.")
        return {"status": "success", "analisis": {
            "xref_discrepancia": xref_res.get("XREF_discrepancia"),
            "varianza_cero": has_variance_zero,
            "score_vectorial": vec_res.get("score_vectorial")
        }}
    except Exception as e:
        conn.close()
        raise HTTPException(status_code=500, detail=f"Error al registrar resultados: {str(e)}")
    finally:
        conn.close()

@app.post("/api/evidencia/anti-palantir")
def activar_anti_palantir(req: APRequest):
    """Dispara el protocolo activo Anti-Palantir y registra la mutación criptográfica."""
    conn = database.get_connection()
    evidencia = conn.execute("SELECT * FROM evidencias WHERE id = ?", (req.evidencia_id,)).fetchone()
    if not evidencia:
        conn.close()
        raise HTTPException(status_code=404, detail="Evidencia no encontrada")
        
    ruta = evidencia["ruta_absoluta"]
    res_ap = AntiPalantir.ejecutar_mitigacion(ruta)
    
    if res_ap["status"] == "success":
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE evidencias SET sha256_mutado = ?, estado_custodia = 'MUTADO_PROTEGIDO' WHERE id = ?",
            (res_ap["mutated_hash"], req.evidencia_id)
        )
        conn.commit()
        database.registrar_custody_log(req.evidencia_id, "ANTI_PALANTIR_API", f"Mitigación ejecutada. Mutated Hash: {res_ap['mutated_hash']}")
        
    conn.close()
    return res_ap
