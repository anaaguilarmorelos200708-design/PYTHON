import random

def seleccionar_jugador_inicial():
    while True:
        eleccion = input("¿Qué jugador inicia? (A/B): ").strip().upper()
        if eleccion in ['A', 'B']:
            return eleccion
        else:
            print("Opción inválida. Por favor, ingresa 'A' o 'B'.")

# Definir jugadores
jugadores = ["A", "B"]

# Seleccionar jugador inicial
jugador_inicial = seleccionar_jugador_inicial()
if jugador_inicial == "B": 
    jugadores.reverse()  # Si inicia B, invertimos el orden

resultados = []
num_rondas = 5
puntos = {'A': 0, 'B': 0}

# Simulación de rondas
for ronda in range(1, num_rondas + 1):
    for jugador in jugadores:
        tiro = random.randint(1, 6)  
        resultados.append({'ronda': ronda, 'jugador': jugador, 'tiro': tiro})
        puntos[jugador] += tiro  # acumula puntos directamente

# Determinar ganador
if puntos['A'] > puntos['B']:
    ganador = 'A'
elif puntos['B'] > puntos['A']:
    ganador = 'B'
else:
    ganador = None 

# Mostrar resultados
print("\nResultados por ronda:")
for r in resultados:
    print(f"Ronda {r['ronda']}: Jugador {r['jugador']} tiró {r['tiro']}")

print("\nPuntajes finales:", puntos)
if ganador:
    print(f"🏆 El ganador es el jugador {ganador}")
else:
    print("🤝 Hubo un empate.")