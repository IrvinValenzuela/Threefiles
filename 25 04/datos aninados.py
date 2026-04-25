import json

# 1. Define un JSON con al menos 3 cursos
json_string = '''
[
    {
        "nombre": "matematica III",
        "código": "PY101",
        "créditos": 4,
        "horario": "Lunes 18:00 - 20:00",
        "prerequisitos": []
    },
    {
        "nombre": "fisica II",
        "código": "ED202",
        "créditos": 3,
        "horario": "Martes 10:00 - 12:00",
        "prerequisitos": ["PY101"]
    },
    {
        "nombre": "cosmovision",
        "código": "IA303",
        "créditos": 5,
        "horario": "Miércoles 15:00 - 17:00",
        "prerequisitos": ["PY101", "ED202"]
    }
]
'''

# 2. Parsea el JSON con json.loads()
cursos = json.loads(json_string)

# 3. Imprime solo los cursos de más de 3 créditos
print("--- Cursos con más de 3 créditos ---")
for curso in cursos:
    if curso["créditos"] > 3:
        print(f"- {curso['nombre']} ({curso['créditos']} créditos)")

# 4. Busca un curso por código
codigo_buscado = "IA303"
print(f"\n--- Buscando curso: {codigo_buscado} ---")
for curso in cursos:
    if curso["código"] == codigo_buscado:
        print(f"Encontrado: {curso['nombre']}")

# 5. Modifica el horario de un curso (ejemplo: ED202)
for curso in cursos:
    if curso["código"] == "ED202":
        curso["horario"] = "Viernes 14:00 - 16:00"
        print(f"\nHorario actualizado para {curso['nombre']}")

# 6. Convierte de vuelta a JSON con json.dumps()
json_actualizado = json.dumps(cursos, indent=4, ensure_ascii=False)


