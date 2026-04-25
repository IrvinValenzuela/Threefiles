
persona = {
    "nombre": "Irvin",
    "edad": 19,
    "ciudad": "Escuintla",
    "lenguaje_favorito": "android studio"
}


persona["universidad"] = "San pablo de Escuintla"


persona["edad"] = 20


print("--- Información del diccionario ---")
for clave, valor in persona.items():
    print(f"{clave.capitalize()}: {valor}")


print("\n--- Verificaciones ---")
if "email" in persona:
    print("El email existe.")
else:
    print("La clave 'email' no se encuentra en el diccionario.")


telefono = persona.get("telefono", "No disponible")
print(f"Teléfono: {telefono}")
