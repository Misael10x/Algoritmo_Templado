import math
import random

# Define las funciones de distancia y evaluación de ruta
def distancia(coord1, coord2):
    lat1 = coord1[0]
    lon1 = coord1[1]
    lat2 = coord2[0]
    lon2 = coord2[1]
    return math.sqrt((lat1 - lat2) ** 2 + (lon1 - lon2) ** 2)

def evalua_ruta(ruta, coord):
    total = 0
    for i in range(0, len(ruta) - 1):
        ciudad1 = ruta[i]
        ciudad2 = ruta[i + 1]
        total += distancia(coord[ciudad1], coord[ciudad2])
    # Cierra el ciclo
    ciudad1 = ruta[-1]
    ciudad2 = ruta[0]
    total += distancia(coord[ciudad1], coord[ciudad2])
    return total

# Algoritmo de Simulated Annealing
def simulated_annealing(ruta, coord):
    T = 20
    T_MIN = 0
    V_enfriamiento = 100

    while T > T_MIN:
        dist_actual = evalua_ruta(ruta, coord)
        for _ in range(1, V_enfriamiento):
            # Intercambio aleatorio de dos ciudades
            i = random.randint(0, len(ruta) - 1)
            j = random.randint(0, len(ruta) - 1)
            ruta_tmp = ruta[:]
            ciudad_tmp = ruta_tmp[i]
            ruta_tmp[i] = ruta_tmp[j]
            ruta_tmp[j] = ciudad_tmp
            dist = evalua_ruta(ruta_tmp, coord)
            delta = dist_actual - dist
            # Criterio de aceptación
            if dist < dist_actual:
                ruta = ruta_tmp[:]
                break
            elif random.random() < math.exp(delta / T):
                ruta = ruta_tmp[:]
                break
        T -= 0.005

    return ruta