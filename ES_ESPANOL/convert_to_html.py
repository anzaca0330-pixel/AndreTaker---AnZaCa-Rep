import markdown
import sys
import os

def convert(md_file):
    with open(md_file, 'r', encoding='utf-8') as f:
        text = f.read()
    
    html_content = markdown.markdown(text, extensions=['tables', 'fenced_code'])
    
    # Add basic styling for printing
    html_template = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8">
        <style>
            body {{ font-family: Arial, sans-serif; line-height: 1.6; max-width: 800px; margin: 0 auto; padding: 20px; }}
            h1, h2, h3 {{ color: #333; }}
            table {{ border-collapse: collapse; width: 100%; margin-bottom: 20px; }}
            th, td {{ border: 1px solid #ddd; padding: 8px; text-align: left; }}
            th {{ background-color: #f2f2f2; }}
            img {{ max-width: 100%; height: auto; }}
            blockquote {{ border-left: 4px solid #ccc; padding-left: 10px; color: #666; font-style: italic; }}
        </style>
    </head>
    <body>
        {html_content}
    </body>
    </html>
    """
    
    html_file = os.path.splitext(md_file)[0] + '.html'
    with open(html_file, 'w', encoding='utf-8') as f:
        f.write(html_template)
    print(f"Converted {md_file} to {html_file}")

files = [
    "/home/andrea-zabala-c/Desktop/ENTREGABLES_FORENSES_E14/ES_ESPANOL/PROYECTO_ESTADISTICO_PSY315.md",
    "/home/andrea-zabala-c/Desktop/ENTREGABLES_FORENSES_E14/ES_ESPANOL/UOPX_PLA_Autobiography.md",
    "/home/andrea-zabala-c/Desktop/ENTREGABLES_FORENSES_E14/ES_ESPANOL/UOPX_PLA_Journal_Template.md"
]

for file in files:
    if os.path.exists(file):
        convert(file)
    else:
        print(f"File not found: {file}")

