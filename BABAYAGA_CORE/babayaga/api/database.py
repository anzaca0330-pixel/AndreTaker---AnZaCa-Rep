import os
import sqlite3
from datetime import datetime, timezone

DB_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "../..", "babayaga_custody.db"))

def get_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    """Inicializa la base de datos de control de custodia y veredictos periciales."""
    conn = get_connection()
    cursor = conn.cursor()
    
    # Tabla de Casos
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS casos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL UNIQUE,
        descripcion TEXT,
        fecha_creacion TEXT NOT NULL
    )
    """)
    
    # Tabla de Evidencias (con campos para cadena de custodia y Anti-Palantir)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS evidencias (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        caso_id INTEGER,
        nombre_archivo TEXT NOT NULL,
        ruta_absoluta TEXT NOT NULL UNIQUE,
        sha256_original TEXT NOT NULL,
        sha256_mutado TEXT,
        estado_custodia TEXT DEFAULT 'INTEGRO',
        fecha_registro TEXT NOT NULL,
        FOREIGN KEY (caso_id) REFERENCES casos(id)
    )
    """)
    
    # Tabla de Resultados de Análisis periciales de BabaYaga
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS analisis_resultados (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        evidencia_id INTEGER UNIQUE,
        exit_code INTEGER,
        discrepancia_xref BOOLEAN,
        xref_detalle TEXT,
        cant_imagenes INTEGER,
        varianza_cero_detectada BOOLEAN,
        contiene_vectores BOOLEAN,
        score_vectorial INTEGER,
        fecha_analisis TEXT NOT NULL,
        FOREIGN KEY (evidencia_id) REFERENCES evidencias(id)
    )
    """)
    
    # Tabla de Bitácora de Cadena de Custodia (Custody Logs)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS custody_logs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        evidencia_id INTEGER,
        fecha_evento TEXT NOT NULL,
        accion TEXT NOT NULL,
        detalles TEXT,
        FOREIGN KEY (evidencia_id) REFERENCES evidencias(id)
    )
    """)
    
    # Insertar un caso por defecto para empezar a trabajar de inmediato
    try:
        fecha_utc = datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
        cursor.execute(
            "INSERT OR IGNORE INTO casos (nombre, descripcion, fecha_creacion) VALUES (?, ?, ?)",
            ("Caso General E14", "Caso base para la auditoría y custodia de actas presidenciales 2026", fecha_utc)
        )
    except Exception:
        pass
        
    conn.commit()
    conn.close()
    print(f"📦 Base de datos de Custodia Forense inicializada en: {DB_PATH}")

# --- Funciones de Conveniencia CRUD ---

def registrar_caso(nombre, descripcion):
    conn = get_connection()
    cursor = conn.cursor()
    fecha_utc = datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
    try:
        cursor.execute(
            "INSERT OR IGNORE INTO casos (nombre, descripcion, fecha_creacion) VALUES (?, ?, ?)",
            (nombre, descripcion, fecha_utc)
        )
        conn.commit()
        # Obtener el ID
        cursor.execute("SELECT id FROM casos WHERE nombre = ?", (nombre,))
        row = cursor.fetchone()
        return row['id']
    except Exception as e:
        print(f"Error al registrar caso: {str(e)}")
        return None
    finally:
        conn.close()

def registrar_evidencia(caso_id, nombre_archivo, ruta_absoluta, sha256_original, sha256_mutado=None, estado_custodia='INTEGRO'):
    conn = get_connection()
    cursor = conn.cursor()
    fecha_utc = datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
    try:
        cursor.execute(
            """INSERT OR REPLACE INTO evidencias 
               (caso_id, nombre_archivo, ruta_absoluta, sha256_original, sha256_mutado, estado_custodia, fecha_registro) 
               VALUES (?, ?, ?, ?, ?, ?, ?)""",
            (caso_id, nombre_archivo, ruta_absoluta, sha256_original, sha256_mutado, estado_custodia, fecha_utc)
        )
        conn.commit()
        cursor.execute("SELECT id FROM evidencias WHERE ruta_absoluta = ?", (ruta_absoluta,))
        row = cursor.fetchone()
        ev_id = row['id']
        
        # Registrar en la bitácora de cadena de custodia
        registrar_custody_log(ev_id, "IMPORT", f"Archivo importado. SHA-256 original: {sha256_original}")
        return ev_id
    except Exception as e:
        print(f"Error al registrar evidencia: {str(e)}")
        return None
    finally:
        conn.close()

def registrar_analisis_resultado(evidencia_id, exit_code, discrepancia_xref, xref_detalle, cant_imagenes, varianza_cero_detectada, contiene_vectores, score_vectorial):
    conn = get_connection()
    cursor = conn.cursor()
    fecha_utc = datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
    try:
        cursor.execute(
            """INSERT OR REPLACE INTO analisis_resultados 
               (evidencia_id, exit_code, discrepancia_xref, xref_detalle, cant_imagenes, varianza_cero_detectada, contiene_vectores, score_vectorial, fecha_analisis) 
               VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)""",
            (evidencia_id, exit_code, discrepancia_xref, xref_detalle, cant_imagenes, varianza_cero_detectada, contiene_vectores, score_vectorial, fecha_utc)
        )
        conn.commit()
        # Registrar en bitácora
        status_msg = "Anomalías encontradas" if (discrepancia_xref or varianza_cero_detectada) else "Estructura limpia"
        registrar_custody_log(evidencia_id, "ANALYZE", f"Análisis forense completado. Diagnóstico: {status_msg}")
    except Exception as e:
        print(f"Error al registrar resultado de análisis: {str(e)}")
    finally:
        conn.close()

def registrar_custody_log(evidencia_id, accion, detalles):
    conn = get_connection()
    cursor = conn.cursor()
    fecha_utc = datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
    try:
        cursor.execute(
            "INSERT INTO custody_logs (evidencia_id, fecha_evento, accion, detalles) VALUES (?, ?, ?, ?)",
            (evidencia_id, fecha_utc, accion, detalles)
        )
        conn.commit()
    except Exception as e:
        print(f"Error en log de custodia: {str(e)}")
    finally:
        conn.close()

def obtener_resumen_caso(caso_id):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT count(*) as total FROM evidencias WHERE caso_id = ?", (caso_id,))
        total = cursor.fetchone()['total']
        
        cursor.execute("""
            SELECT count(*) as total_anomalas FROM analisis_resultados ar
            JOIN evidencias e ON ar.evidencia_id = e.id
            WHERE e.caso_id = ? AND (ar.discrepancia_xref = 1 OR ar.varianza_cero_detectada = 1)
        """, (caso_id,))
        total_anomalas = cursor.fetchone()['total_anomalas']
        
        return {
            "total_archivos": total,
            "total_anomalos": total_anomalas,
            "anomalias_porcentaje": (total_anomalas / total * 100.0) if total > 0 else 0.0
        }
    except Exception as e:
        print(f"Error al obtener resumen: {str(e)}")
        return None
    finally:
        conn.close()

if __name__ == "__main__":
    init_db()
