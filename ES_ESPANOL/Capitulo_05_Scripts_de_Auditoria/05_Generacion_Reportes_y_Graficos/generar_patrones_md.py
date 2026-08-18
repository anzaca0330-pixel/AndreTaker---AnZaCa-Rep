import csv
from collections import defaultdict
import os

def analyze():
    unified_csv = "/home/andrea-zabala-c/Desktop/ENTREGABLES_FORENSES_E14/REPORTE_XREF_DEEPFAKE.csv"
    output_md = "/home/andrea-zabala-c/.gemini/antigravity-ide/brain/4d9eb513-0e97-432b-b53b-e5a7ff1d21fd/patrones_anomalias_geograficas.md"
    
    # department -> municipio -> zona -> puesto -> { total, deepfakes, xref, trailer }
    geo_stats = defaultdict(lambda: defaultdict(lambda: defaultdict(lambda: defaultdict(lambda: {'total': 0, 'deepfake': 0, 'xref': 0, 'trailer': 0}))))
    
    # For higher level aggregation
    dpto_stats = defaultdict(lambda: {'total': 0, 'anomalies': 0})
    mun_stats = defaultdict(lambda: {'total': 0, 'anomalies': 0, 'name': ''})

    if not os.path.exists(unified_csv):
        print(f"File {unified_csv} not found.")
        return

    with open(unified_csv, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            dpto = row.get('departamento', 'N/A')
            mun = row.get('municipio', 'N/A')
            zona = row.get('zona', 'N/A')
            puesto = row.get('puesto', 'N/A')
            
            xref = row.get('resultado_xref', '')
            deepfake = row.get('Diagnostico_DeepFake', '')
            
            is_anomaly = False
            
            geo_stats[dpto][mun][zona][puesto]['total'] += 1
            dpto_stats[dpto]['total'] += 1
            
            # Use mun code as key, store a readable string
            mun_key = f"{dpto}-{mun}"
            mun_stats[mun_key]['total'] += 1
            mun_stats[mun_key]['name'] = f"Dpto {dpto} - Mun {mun}"
            
            if "DEEPFAKE SINTÉTICO" in deepfake:
                geo_stats[dpto][mun][zona][puesto]['deepfake'] += 1
                is_anomaly = True
                
            if "CORRUPTO_XREF" in xref:
                geo_stats[dpto][mun][zona][puesto]['xref'] += 1
                is_anomaly = True
                
            if "CORRUPTO_TRAILER" in xref:
                geo_stats[dpto][mun][zona][puesto]['trailer'] += 1
                is_anomaly = True
                
            if is_anomaly:
                dpto_stats[dpto]['anomalies'] += 1
                mun_stats[mun_key]['anomalies'] += 1

    # Sorting
    sorted_dptos = sorted(dpto_stats.items(), key=lambda x: x[1]['anomalies'], reverse=True)
    sorted_muns = sorted(mun_stats.items(), key=lambda x: x[1]['anomalies'], reverse=True)
    
    with open(output_md, 'w', encoding='utf-8') as out:
        out.write("# 🗺️ Patrones Geográficos de Anomalías E-14\n\n")
        out.write("> [!IMPORTANT]\n")
        out.write("> Este documento consolida las anomalías estructurales (XREF/Trailer) y visuales (Deepfakes) por ubicación geográfica.\n\n")
        
        out.write("## 📍 Top 10 Departamentos con más Anomalías\n\n")
        out.write("| Departamento | Total Mesas Analizadas | Anomalías Detectadas | Porcentaje de Afectación |\n")
        out.write("|---|---|---|---|\n")
        
        for dpto, stats in sorted_dptos[:10]:
            if stats['total'] == 0: continue
            pct = (stats['anomalies'] / stats['total']) * 100
            if pct > 0:
                out.write(f"| **{dpto}** | {stats['total']:,} | <span style='color:red'>**{stats['anomalies']:,}**</span> | <span style='color:red'>**{pct:.1f}%**</span> |\n")
            else:
                out.write(f"| {dpto} | {stats['total']:,} | {stats['anomalies']:,} | {pct:.1f}% |\n")
                
        out.write("\n## 🏙️ Top 15 Municipios con más Anomalías\n\n")
        out.write("| Municipio | Total Mesas Analizadas | Anomalías Detectadas | Porcentaje de Afectación |\n")
        out.write("|---|---|---|---|\n")
        
        for mun_key, stats in sorted_muns[:15]:
            if stats['total'] == 0: continue
            pct = (stats['anomalies'] / stats['total']) * 100
            if pct > 0:
                out.write(f"| **{stats['name']}** | {stats['total']:,} | <span style='color:red'>**{stats['anomalies']:,}**</span> | <span style='color:red'>**{pct:.1f}%**</span> |\n")
            else:
                out.write(f"| {stats['name']} | {stats['total']:,} | {stats['anomalies']:,} | {pct:.1f}% |\n")

        # Zona level
        out.write("\n## 🕵️‍♂️ Patrones Críticos a nivel de Puesto de Votación\n\n")
        out.write("Los siguientes puestos de votación muestran una concentración inusual de anomalías (más de 10 anomalías en el mismo puesto):\n\n")
        
        out.write("| Puesto (Dpto-Mun-Zona-Pto) | Mesas | <span style='color:red'>Deepfakes</span> | <span style='color:red'>XREF Corruptos</span> | <span style='color:red'>Trailer Corruptos</span> |\n")
        out.write("|---|---|---|---|---|\n")
        
        critical_puestos = []
        for dpto, muns in geo_stats.items():
            for mun, zonas in muns.items():
                for zona, puestos in zonas.items():
                    for puesto, s in puestos.items():
                        total_ano = s['deepfake'] + s['xref'] + s['trailer']
                        if total_ano >= 10:
                            critical_puestos.append({
                                'name': f"Dpto {dpto} - Mun {mun} - Zona {zona} - {puesto}",
                                'total': s['total'],
                                'deepfake': s['deepfake'],
                                'xref': s['xref'],
                                'trailer': s['trailer'],
                                'total_ano': total_ano
                            })
                            
        critical_puestos.sort(key=lambda x: x['total_ano'], reverse=True)
        
        for p in critical_puestos[:30]: # top 30
            out.write(f"| **{p['name']}** | {p['total']} | <span style='color:red'>**{p['deepfake']}**</span> | <span style='color:red'>**{p['xref']}**</span> | <span style='color:red'>**{p['trailer']}**</span> |\n")
            
        out.write("\n\n> [!NOTE]\n")
        out.write("> Los datos han sido resaltados en rojo (`<span style='color:red'>`) como lo solicitaste para identificar visualmente los clústers geográficos donde operó el software sintético.\n")
        
    print("Report generated.")

if __name__ == '__main__':
    analyze()
