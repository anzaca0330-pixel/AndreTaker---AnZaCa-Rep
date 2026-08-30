import subprocess
import os
import re

class XrefAnalyzer:
    @staticmethod
    def _xref_via_qpdf(pdf_path: str) -> dict:
        """Audita la estructura interna (XREF) usando la herramienta del sistema qpdf."""
        try:
            resultado = subprocess.run(
                ['qpdf', '--check', pdf_path],
                capture_output=True,
                text=True
            )
            
            stdout_clean = resultado.stdout.strip()
            stderr_clean = resultado.stderr.strip()
            
            has_xref_warning = ('reported number of objects' in stderr_clean) or ('reported number of objects' in stdout_clean)
            
            return {
                'exit_code': resultado.returncode,
                'stdout': stdout_clean,
                'stderr': stderr_clean,
                'XREF_discrepancia': has_xref_warning,
                'detalle': stderr_clean if stderr_clean else (stdout_clean if stdout_clean else 'Estructura sin advertencias'),
                'metodo': 'qpdf'
            }
        except Exception as e:
            return {
                'exit_code': -1,
                'XREF_discrepancia': False,
                'detalle': f'Error en ejecución de qpdf: {str(e)}',
                'metodo': 'qpdf'
            }

    @staticmethod
    def _xref_via_raw(pdf_path: str) -> dict:
        """
        Método alternativo ("Llama al diablo"): Parsea el binario del PDF directamente 
        para auditar la tabla XREF sin dependencias de qpdf.
        """
        try:
            with open(pdf_path, 'rb') as f:
                content = f.read()

            if not content.startswith(b'%PDF'):
                return {
                    'exit_code': -1,
                    'XREF_discrepancia': False,
                    'detalle': 'No es un archivo PDF válido (cabecera inválida)',
                    'metodo': 'raw_binary'
                }

            # Buscar la declaración de tamaño en el trailer (/Size)
            size_matches = re.findall(rb'/Size\s+(\d+)', content)
            # Buscar objetos declarados (N 0 obj)
            obj_matches = re.findall(rb'(\d+)\s+0\s+obj', content)

            declared = int(size_matches[-1]) if size_matches else None
            actual_max = max(int(n) for n in obj_matches) if obj_matches else None

            scar = False
            detalle = 'Estructura del PDF íntegra (análisis binario nativo)'

            if declared and actual_max:
                expected = actual_max + 1
                if declared != expected:
                    scar = True
                    detalle = (f'[MÉTODO ALTERNATIVO — DIABLO ACTIVO] '
                               f'reported number of objects ({declared}) is not one plus '
                               f'the highest object number ({actual_max})')

            return {
                'exit_code': 0,
                'stdout': '',
                'stderr': detalle,
                'XREF_discrepancia': scar,
                'detalle': detalle,
                'metodo': 'raw_binary'
            }
        except Exception as e:
            return {
                'exit_code': -1,
                'XREF_discrepancia': False,
                'detalle': f'Error en análisis binario: {str(e)}',
                'metodo': 'raw_binary'
            }

    @classmethod
    def analizar_estructura(cls, pdf_path: str) -> dict:
        """Audita la estructura interna (XREF) con escalado automático al parser binario."""
        if not os.path.exists(pdf_path):
            return {
                'exit_code': -1,
                'XREF_discrepancia': False,
                'detalle': f'Archivo no encontrado: {pdf_path}',
                'metodo': 'ninguno'
            }
            
        # Comprobar si qpdf está disponible en el sistema
        qpdf_disponible = subprocess.run(['which', 'qpdf'], capture_output=True).returncode == 0
        if qpdf_disponible:
            return cls._xref_via_qpdf(pdf_path)
        else:
            return cls._xref_via_raw(pdf_path)
