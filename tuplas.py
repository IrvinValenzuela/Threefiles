coordenadas = (14.297777777778, -90.786944444444)
colores_rgb = (225, 128, 0)

lat, lon = coordenadas

print(f"altitud: {lat}, Longitud: {lon}")


def calcular_estadisticas(numeros):
    minimo = min(numeros)
    maximo = max(numeros)
    promedio = sum(numeros) / len(numeros)
    
    # Retorna una tupla
    return (minimo, maximo, promedio)


distancias = {
    ("Guate", "Escuintla"): 58,
    ("Guate", "Antigua"): 45,
}

# Acceder a un valor usando la tupla como clave
distancia_antigua = distancias[("Guate", "Antigua")]
print(f"Distancia a Antigua: {distancia_antigua} km")

mi_tupla = (1, 2, 3)

try:
    mi_tupla[0] = 10
except TypeError as e:
    print(f"Error: {e}")

# Explicación:
# Las tuplas son INMUTABLES. Esto significa que una vez creadas, 
# no se pueden modificar, agregar ni eliminar sus elementos. 
# Si necesitas una estructura modificable, deberías usar una lista [].




