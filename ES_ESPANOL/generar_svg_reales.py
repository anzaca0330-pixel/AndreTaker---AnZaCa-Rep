import csv
import math

def generate_benford_svg():
    csv_file = "/home/andrea-zabala-c/Desktop/ENTREGABLES_FORENSES_E14/ES_ESPANOL/Capitulo_07_Bases_de_Datos_CSV/anomalias_benford_2BL_nacional_abelardo.csv"
    counts = {str(i): 0 for i in range(10)}
    total = 0
    with open(csv_file, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            digit = str(row['segundo_digito']).strip()
            if digit in counts:
                counts[digit] += 1
                total += 1
                
    freqs = {d: (counts[d]/total)*100 if total > 0 else 0 for d in counts}
    benford_probs = [11.968, 11.389, 10.882, 10.433, 10.031, 9.668, 9.337, 9.035, 8.757, 8.500]
    
    # SVG construction
    svg = ['<svg width="800" height="500" xmlns="http://www.w3.org/2000/svg">']
    svg.append('<rect width="100%" height="100%" fill="white"/>')
    svg.append('<text x="400" y="30" font-family="Arial" font-size="20" font-weight="bold" text-anchor="middle">Análisis 2BL: Anomalía Extrema en Segundo Dígito (Datos Reales)</text>')
    
    # Axes
    svg.append('<line x1="50" y1="400" x2="750" y2="400" stroke="black" stroke-width="2"/>')
    svg.append('<line x1="50" y1="50" x2="50" y2="400" stroke="black" stroke-width="2"/>')
    
    # Y-axis labels
    for i in range(0, 25, 5):
        y_pos = 400 - (i * 15)
        svg.append(f'<text x="40" y="{y_pos+5}" font-family="Arial" font-size="12" text-anchor="end">{i}%</text>')
        svg.append(f'<line x1="45" y1="{y_pos}" x2="750" y2="{y_pos}" stroke="#ddd" stroke-width="1"/>')
        
    # X-axis labels and bars
    bar_width = 20
    for i in range(10):
        x_base = 100 + i * 65
        svg.append(f'<text x="{x_base + bar_width}" y="420" font-family="Arial" font-size="14" text-anchor="middle">{i}</text>')
        
        # Real Freq Bar (Red)
        real_h = freqs[str(i)] * 15
        svg.append(f'<rect x="{x_base}" y="{400 - real_h}" width="{bar_width}" height="{real_h}" fill="salmon" stroke="black"/>')
        
        # Benford Bar (Blue)
        benf_h = benford_probs[i] * 15
        svg.append(f'<rect x="{x_base + bar_width}" y="{400 - benf_h}" width="{bar_width}" height="{benf_h}" fill="lightblue" stroke="black"/>')
        
    # Legend
    svg.append('<rect x="550" y="50" width="15" height="15" fill="salmon" stroke="black"/>')
    svg.append('<text x="575" y="62" font-family="Arial" font-size="12">Frecuencia Observada (Real)</text>')
    svg.append('<rect x="550" y="75" width="15" height="15" fill="lightblue" stroke="black"/>')
    svg.append('<text x="575" y="87" font-family="Arial" font-size="12">Distribución Benford</text>')
    
    svg.append('</svg>')
    
    with open("/home/andrea-zabala-c/Desktop/ENTREGABLES_FORENSES_E14/ES_ESPANOL/real_benford_histogram.svg", "w") as f:
        f.write("\n".join(svg))

def generate_variance_svg():
    csv_file = "/home/andrea-zabala-c/Desktop/ENTREGABLES_FORENSES_E14/ES_ESPANOL/Capitulo_07_Bases_de_Datos_CSV/ESTUDIO_ESTADISTICO_NACIONAL.csv"
    data = []
    with open(csv_file, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            try:
                mesas = float(row['mesas'])
                var_e = float(row['var_espriella'])
                if var_e >= 0:
                    data.append((mesas, var_e))
            except:
                pass

    svg = ['<svg width="800" height="500" xmlns="http://www.w3.org/2000/svg">']
    svg.append('<rect width="100%" height="100%" fill="white"/>')
    svg.append('<text x="400" y="30" font-family="Arial" font-size="20" font-weight="bold" text-anchor="middle">ANOVA: Colapso de Varianza Nacional (Datos Reales)</text>')
    
    svg.append('<line x1="50" y1="450" x2="750" y2="450" stroke="black" stroke-width="2"/>')
    svg.append('<line x1="50" y1="50" x2="50" y2="450" stroke="black" stroke-width="2"/>')
    
    max_mesas = max(d[0] for d in data) if data else 100
    max_var = max(d[1] for d in data) if data else 100
    
    # Umbral
    threshold_y = 450 - (6.25 / max_var) * 400
    svg.append(f'<line x1="50" y1="{threshold_y}" x2="750" y2="{threshold_y}" stroke="darkred" stroke-width="2" stroke-dasharray="5,5"/>')
    svg.append(f'<text x="55" y="{threshold_y - 5}" font-family="Arial" font-size="12" fill="darkred">Umbral Anómalo (Std=2.5)</text>')
    
    # Points
    for mesas, var_e in data:
        cx = 50 + (mesas / max_mesas) * 700
        cy = 450 - (var_e / max_var) * 400
        color = "red" if var_e < 100 else "blue"
        r = "5" if var_e < 100 else "3"
        svg.append(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{color}" stroke="black" opacity="0.7"/>')
        
    svg.append('</svg>')
    
    with open("/home/andrea-zabala-c/Desktop/ENTREGABLES_FORENSES_E14/ES_ESPANOL/real_variance_scatter.svg", "w") as f:
        f.write("\n".join(svg))

if __name__ == "__main__":
    generate_benford_svg()
    generate_variance_svg()
    print("Gráficas SVG reales generadas exitosamente.")
