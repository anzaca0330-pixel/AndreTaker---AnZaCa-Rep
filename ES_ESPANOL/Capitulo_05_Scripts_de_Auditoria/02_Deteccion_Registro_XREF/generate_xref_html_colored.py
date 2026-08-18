# generate_xref_html_colored.py
"""Generate an HTML table from REPO_XREF_DEEPFAKE.csv with rows colored:
- Green (#c3e6cb) if both XREF alteration (contains 'CORRUPTO') and DeepFake status are present.
- Red (#f5c6cb) if only one of them is present.
- Light Blue (#bee5eb) if clean (neither is present).
"""
import csv
import os

BASE_DIR = "/home/andrea-zabala-c/Desktop/ENTREGABLES_FORENSES_E14"
CSV_PATH = os.path.join(BASE_DIR, "REPORTE_XREF_DEEPFAKE.csv")
OUTPUT_HTML = os.path.join(BASE_DIR, "XREF_ALTERACIONES_COLOREADAS.html")

def load_rows(csv_path):
    with open(csv_path, newline="", encoding="utf-8") as f:
        reader = csv.reader(f)
        header = next(reader)
        rows = [header]
        for row in reader:
            rows.append(row)
    return rows

rows = load_rows(CSV_PATH)

html = [
    "<!DOCTYPE html>",
    "<html lang='es'>",
    "<head>",
    "  <meta charset='UTF-8'>",
    "  <title>Listado XREF con Alteraciones coloreadas</title>",
    "  <style>",
    "    body {font-family:Arial,Helvetica,sans-serif;background:#f5f5f5;color:#333;}",
    "    table {border-collapse:collapse;width:100%;margin-top:20px;}",
    "    th, td {padding:8px 12px;border:1px solid #ccc;}",
    "    th {background:#333;color:#fff;position:sticky;top:0;z-index:2;}",
    "    .red {background:#ffcccc;}",
    "    .blue {background:#cce5ff;}",
    "    .green {background:#d4edda;}",
    "  </style>",
    "</head>",
    "<body>",
    "<h1>Listado Individual XREF – filas coloreadas</h1>",
    "<table>"
]

# header row
header = rows[0]
html.append("<tr>")
for col in header:
    html.append(f"  <th>{col}</th>")
html.append("</tr>")

# data rows
for row in rows[1:]:
    xref_status = row[1].strip().upper() if len(row) > 1 else ""
    deepfake_status = row[7].strip() if len(row) > 7 else ""
    
    has_xref = "CORRUPTO" in xref_status
    has_df = bool(deepfake_status)
    
    if has_xref and has_df:
        css_class = "green"
    elif has_xref or has_df:
        css_class = "red"
    else:
        css_class = "blue"
        
    html.append(f"<tr class='{css_class}'>")
    for cell in row:
        html.append(f"  <td>{cell}</td>")
    html.append("</tr>")

html.extend(["</table>", "</body>", "</html>"])

with open(OUTPUT_HTML, "w", encoding="utf-8") as f:
    f.write("\n".join(html))

print(f"✅ HTML generado: {OUTPUT_HTML}")
