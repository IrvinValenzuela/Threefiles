def agregar_contacto(agenda):
    nombre = input("Ingrese el nombre: ").strip()
    if not nombre:
        print("Error: El nombre no puede estar vacío.")
        return
    
    telefono = input("Ingrese el teléfono: ")
    email = input("Ingrese el email: ")
    
    nuevo_contacto = {
        "nombre": nombre,
        "telefono": telefono,
        "email": email
    }
    agenda.append(nuevo_contacto)
    print(f"Contacto '{nombre}' agregado con éxito.")

def buscar_contacto(agenda):
    nombre_buscar = input("Nombre a buscar: ").strip().lower()
    encontrado = False
    for contacto in agenda:
        # Uso de .get() para acceso seguro
        if contacto.get("nombre").lower() == nombre_buscar:
            print(f"\n--- Contacto Encontrado ---")
            print(f"Nombre: {contacto.get('nombre')}")
            print(f"Teléfono: {contacto.get('telefono')}")
            print(f"Email: {contacto.get('email')}")
            encontrado = True
            break
    if not encontrado:
        print("Contacto no encontrado.")

def mostrar_contactos(agenda):
    if not agenda:
        print("La agenda está vacía.")
        return
    
    print("\n--- Lista de Contactos ---")
    for i, contacto in enumerate(agenda, 1):
        print(f"{i}. {contacto.get('nombre')} - {contacto.get('telefono')} ({contacto.get('email')})")

def eliminar_contacto(agenda):
    nombre_eliminar = input("Nombre del contacto a eliminar: ").strip().lower()
    for contacto in agenda:
        if contacto.get("nombre").lower() == nombre_eliminar:
            agenda.remove(contacto)
            print(f"Contacto '{contacto.get('nombre')}' eliminado.")
            return
    print("No se encontró el contacto para eliminar.")

def menu():
    # Requisito: Guardar contactos en lista de diccionarios
    agenda_contactos = []
    
    # Requisito: Usar while True para el menú principal
    while True:
        print("\n--- Agenda de Contactos ---")
        print("1. Agregar contacto")
        print("2. Buscar contacto por nombre")
        print("3. Mostrar todos los contactos")
        print("4. Eliminar contacto")
        print("5. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            agregar_contacto(agenda_contactos)
        elif opcion == "2":
            buscar_contacto(agenda_contactos)
        elif opcion == "3":
            mostrar_contactos(agenda_contactos)
        elif opcion == "4":
            eliminar_contacto(agenda_contactos)
        elif opcion == "5":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida, intente de nuevo.")

if __name__ == "__main__":
    menu()
