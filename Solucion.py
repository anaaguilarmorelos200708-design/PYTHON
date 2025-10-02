# Versión con 20 ERRORES a propósito
import random
 # ERROR 1: se sobrescribe el módulo random con un entero
def seleccionar_jugador_inicial():
    while True:
        eleccion = input("¿Qué jugador inicia? (A/B): ").strip().upper()  # ERROR 2: lower() pero se valida contra mayúsculas
        if eleccion in ['A', 'B']:  # nunca coincide por el ERROR 2 → bucle infinito si se llegara a usar bien
            return eleccion
        else:
            print("Opción inválida. Por favor, ingresa 'A' o 'B'.")

# Definir jugadores
jugadores = ["A", "B"]  # ERROR 3: tupla (inmutable)

# Seleccionar jugador inicial
jugador_inicial = seleccionar_jugador_inicial()
if jugador_inicial == "B": # ERROR 19: variable “ruido”/no usada
   jugadores.reverse()  # ERROR 4: las tuplas no tienen reverse()

resultados = []        # ERROR 5: debería ser lista, dict no tiene append
num_rondas = 5     # ERROR 6: cadena en lugar de entero
puntos = {'A': 0, 'B': 0}  # ERROR 7: clave de B en minúscula

# Simulación de rondas
for ronda in range(1, num_rondas + 1):  # ERROR 8: sumando 1 a una cadena; TypeError
    for jugador in jugadores:
        tiro = random.randint(1, 6)      # ERROR 9: 'random' ahora es int, no módulo        # ERROR 20: redondeo innecesario de un int
        resultados.append({ 'ronda': ronda,'jugador': jugador,'tiro': tiro })              # ERROR 5 se manifiesta aquí: dict no tiene append
        puntos[jugador] += tiro # ERROR 10: clave incorrecta, debería ser 'ronda'
                    # ERROR 11: clave mal escrita, debería ser 'jugador'
            
        
           # ERROR 14: KeyError cuando jugador == 'B' (por ERROR 7)

# Determinar ganador
if puntos['A'] > puntos['B']:            # ERROR 15: clave 'C' no existe
    ganador = 'A'
elif puntos['B'] > puntos['A']:
    ganador = 'B'
else:
    ganador = None                      # ERROR 16: se esperaba None para empate

# Mostrar resultados
print("\nResultados por ronda:")
for r in resultados:
    print(f"Ronda {r['ronda']} Jugador {r['jugador']} tiro {r['tiro']}")  # ERROR 12, 13: claves mal nombradas

print("\nPuntajes finales:",puntos)      # ERROR 17: variable 'punto' no existe
if ganador:
    print(f"🏆 El ganador es el jugador: {ganador}")  # ERROR 18: 'ganadorr' no existe
else:
    print("🤝 Hubo un empate.")
