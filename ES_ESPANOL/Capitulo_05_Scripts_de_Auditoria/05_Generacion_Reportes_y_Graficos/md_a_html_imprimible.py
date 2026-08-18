import os
import sys

def create_html_wrapper(md_file_path):
    if not os.path.exists(md_file_path):
        return
        
    with open(md_file_path, 'r', encoding='utf-8') as f:
        md_content = f.read()
        
    # Escapar comillas y saltos de línea para JS
    md_escaped = md_content.replace('\\', '\\\\').replace('`', '\\`').replace('$', '\\$')
    
    html_content = f"""<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Imprimir a PDF</title>
    <script src="https://cdn.jsdelivr.net/npm/marked/marked.min.js"></script>
    <style>
        body {{ font-family: Arial, sans-serif; line-height: 1.6; max-width: 800px; margin: 0 auto; padding: 40px; color: black; background: white; }}
        h1, h2, h3 {{ color: #2c3e50; }}
        table {{ border-collapse: collapse; width: 100%; margin-bottom: 20px; }}
        th, td {{ border: 1px solid #ddd; padding: 8px; text-align: left; }}
        th {{ background-color: #f2f2f2; }}
        @media print {{
            body {{ padding: 0; }}
            .no-print {{ display: none; }}
        }}
    </style>
</head>
<body>
    <div class="no-print" style="background:#f1c40f; padding:10px; text-align:center; font-weight:bold; margin-bottom:20px;">
        Presiona Ctrl + P (o Cmd + P) para guardar este documento como PDF.
    </div>
    <div id="content"></div>
    <script>
        const markdownText = `{md_escaped}`;
        document.getElementById('content').innerHTML = marked.parse(markdownText);
    </script>
</body>
</html>"""

    html_file = md_file_path.replace('.md', '.html')
    with open(html_file, 'w', encoding='utf-8') as f:
        f.write(html_content)
    print(f"Generado: {html_file}")

files_to_convert = [
    '/home/andrea-zabala-c/Desktop/ENTREGABLES_FORENSES_E14/EDICTO_EMPLAZAMIENTO.md',
    '/home/andrea-zabala-c/Desktop/ENTREGABLES_FORENSES_E14/MANIFESTO_TESTIGO_DIGITAL_ES.md',
    '/home/andrea-zabala-c/Desktop/ENTREGABLES_FORENSES_E14/MANIFESTO_TESTIGO_DIGITAL_EN.md'
]

for file in files_to_convert:
    create_html_wrapper(file)
