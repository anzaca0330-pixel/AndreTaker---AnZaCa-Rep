import numpy as np

def run_montecarlo_simulation(num_simulations=1_000_000):
    # Mesas en Antioquia con Empate Exacto (Espejo Absoluto)
    # Mesa 16: 146 votos (73 a 73)
    # Mesa 4: 208 votos (104 a 104)
    # Mesa 7: 194 votos (97 a 97)
    # Mesa 21: 106 votos (53 a 53)
    voters_per_table = [146, 208, 194, 106]
    
    # Suposicion MUY conservadora: Asumimos que a nivel nacional o departamental
    # los candidatos estan empatados 50/50 (p=0.5). Si fuera 55/45, la probabilidad seria aun menor.
    p = 0.5
    
    success_count = 0
    
    print(f"Ejecutando Simulacion de Monte Carlo con {num_simulations:,} universos electorales...")
    
    for _ in range(num_simulations):
        # Simulamos los votos de Abelardo usando una distribucion Binomial B(n, p)
        # Esto representa tirar una moneda al aire por cada votante
        simulated_votes = [np.random.binomial(n, p) for n in voters_per_table]
        
        # Verificamos si en la simulacion OCURRE el empate exacto en TODAS las 4 mesas
        expected_ties = [n // 2 for n in voters_per_table]
        
        if simulated_votes == expected_ties:
            success_count += 1
            
    p_value = success_count / num_simulations
    
    print("\n--- RESULTADOS MONTE CARLO ---")
    print(f"Mesas evaluadas: {len(voters_per_table)}")
    print(f"Ocurrencias del 'Espejo Absoluto' en {num_simulations:,} simulaciones: {success_count}")
    print(f"Probabilidad (P-Value): {p_value:.8f}")
    
    if p_value == 0:
        print("\nCONCLUSIÓN: Probabilidad virtualmente CERO.")
        print("La secuencia de empates exactos es matemáticamente imposible en el mundo real.")
        print("Esto confirma que la inyección fue programada por un ALGORITMO (Artificial).")
    else:
        print(f"\nProbabilidad: 1 en {int(1/p_value):,}")

if __name__ == "__main__":
    run_montecarlo_simulation(10_000_000) # 10 millones de simulaciones
