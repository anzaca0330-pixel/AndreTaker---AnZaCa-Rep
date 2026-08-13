# Diagrama Forense: Redirección de Transmisión (Spoofing de Códigos QR)

El siguiente diagrama esquematiza cómo el acta original de una mesa fue desviada informáticamente hacia el ID de otra mesa en el sistema central de consolidación, explotando la arquitectura de escaneo automático de la empresa contratista de transmisión.

> [!CAUTION]
> **🔴 PRUEBA DE REDIRECCIÓN MASIVA**
> Este diagrama ilustra el hallazgo documentado en la investigación (Pilar #3), donde la superposición de una capa con un Código QR falso logró secuestrar el flujo de datos del escáner en tiempo real, engañando a la base de datos nacional.

```mermaid
graph TD
    classDef acta fill:#0f172a,stroke:#3b82f6,stroke-width:2px,color:#fff
    classDef falso fill:#ef4444,stroke:#7f1d1d,stroke-width:2px,color:#fff
    classDef normal fill:#1e293b,stroke:#64748b,stroke-width:1px,color:#fff
    classDef final fill:#166534,stroke:#14532d,stroke-width:2px,color:#fff
    
    A["📄 ACTA FÍSICA ORIGINAL (Mesa 'A')\nTotal Votos: 150"]:::acta
    
    B["🟦 Código QR Legítimo\nPayload Hash: 1ffd79f75..."]:::acta
    
    A --> B
    
    C{"🤖 INTERVENCIÓN DE SOFTWARE"}:::falso
    
    D["🟥 CÓDIGO QR FALSO (Inyectado encima)\nPayload Hash: 6f6d0c387..."]:::falso
    
    B -- "Ruta interceptada por" --> C
    C --> D
    
    E["🖨️ Escáner de Transmisión (Disproel/Indra)"]:::normal
    
    D -- "El lector óptico captura la capa superior" --> E
    
    F["💻 Servidor Central de Consolidación"]:::normal
    
    E -- "Envía datos al ID que dicta el QR" --> F
    
    G[("🗄️ Base de Datos: MESA 'B' (Destino Falso)\nTotal Votos Sumados: 150")]:::falso
    
    F --> G
```

## Interpretación Pericial del Flujo:
1. **Entró por aquí (Mesa A):** El jurado diligenció el documento oficial físico asignado a su mesa.
2. **Intervención:** El *software* malicioso superpuso una capa transparente con un QR falso (y su respectivo hash/payload alterado) antes o durante la fase de digitalización.
3. **Salió por aquí (Mesa B):** Al pasar por las máquinas automatizadas de transmisión, el escáner leyó ciegamente el QR superior y envió los resultados a la base de datos, adjudicándolos al ID de la Mesa B.
