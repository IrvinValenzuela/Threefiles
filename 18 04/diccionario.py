# 1. Crear el diccionario inicia
# Los diccionarios usan llaves {} y pares clave: valor
persona = {
    "nombre": "Irvin",
    "edad": 19,
    "ciudad": "Escuintla",
    "lenguaje_favorito": "android studio"
}

# 2. Agregar una nueva clave 'universidad'
# Simplemente asignas un valor a la nueva clave usando corchetes
persona["universidad"] = "San pablo de Escuintla"

# 3. Modificar el valor de 'edad'
# Se usa la misma sintaxis que para agregar, pero con una clave que ya existe
persona["edad"] = 20

# 4. Iterar con .items() e imprimir cada par
# .items() devuelve tanto la clave como el valor en cada vuelta del ciclo
print("--- Información del diccionario ---")
for clave, valor in persona.items():
    print(f"{clave.capitalize()}: {valor}")

# 5. Verificar si 'email' existe con 'in'
# 'in' busca únicamente entre las llaves del diccionario
print("\n--- Verificaciones ---")
if "email" in persona:
    print("El email existe.")
else:
    print("La clave 'email' no se encuentra en el diccionario.")

# 6. Use .get() para acceder a 'telefono' sin error
# Si usaras persona["telefono"] el programa fallaría. 
# .get() devuelve 'None' (o un mensaje personalizado) si la clave no existe.
telefono = persona.get("telefono", "No disponible")
print(f"Teléfono: {telefono}")
