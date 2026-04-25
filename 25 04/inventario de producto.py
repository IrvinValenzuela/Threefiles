import json

# Lista principal para almacenar los productos
inventario = []

def agregar_producto(nombre, precio, cantidad, categoria):
    producto = {
        "nombre": nombre,
        "precio": precio,
        "cantidad": cantidad,
        "categoria": categoria
    }
    inventario.append(producto)
    print(f"Producto '{nombre}' agregado exitosamente.")

def buscar_producto(termino):
    resultados = [p for p in inventario if termino.lower() in p["nombre"].lower() or termino.lower() in p["categoria"].lower()]
    return resultados

def actualizar_cantidad(nombre, cambio):
    for producto in inventario:
        if producto["nombre"].lower() == nombre.lower():
            producto["cantidad"] += cambio
            print(f"Nueva cantidad de {nombre}: {producto['cantidad']}")
            return
    print("Producto no encontrado.")

def calcular_valor_total():
    return sum(p["precio"] * p["cantidad"] for p in inventario)

def stock_bajo():
    return [p for p in inventario if p["cantidad"] < 5]

def exportar_a_json():
    return json.dumps(inventario, indent=4, ensure_ascii=False)


print(f"\nValor total: ${calcular_valor_total():.2f}")
print("\nProductos con stock bajo:", stock_bajo())

# Exportar
json_string = exportar_a_json()
print("\nInventario en formato JSON:")
print(json_string)

def menu():
    while True:
        print("\n--- Menú de Inventario ---")
        print("1. Agregar producto")
        print("2. Buscar producto")
        print("3. Actualizar cantidad")
        print("4. Calcular valor total")
        print("5. Mostrar productos con stock bajo")
        print("6. Exportar a JSON")
        print("7. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre = input("Nombre del producto: ")
            precio = float(input("Precio: "))
            cantidad = int(input("Cantidad: "))
            categoria = input("Categoría: ")
            agregar_producto(nombre, precio, cantidad, categoria)
        elif opcion == "2":
            termino = input("Ingrese el término de búsqueda: ")
            resultados = buscar_producto(termino)
            if resultados:
                for p in resultados:
                    print(p)
            else:
                print("No se encontraron productos.")
        elif opcion == "3":
            nombre = input("Nombre del producto a actualizar: ")
            cambio = int(input("Cantidad a agregar (negativo para reducir): "))
            actualizar_cantidad(nombre, cambio)
        elif opcion == "4":
            print(f"Valor total del inventario: ${calcular_valor_total():.2f}")
        elif opcion == "5":
            bajos = stock_bajo()
            if bajos:
                for p in bajos:
                    print(p)
            else:
                print("No hay productos con stock bajo.")
        elif opcion == "6":
            print(exportar_a_json())
        elif opcion == "7":
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    menu()

