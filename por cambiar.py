coordenadas = (14.297777777778, -90.786944444444)
colores_rgb = (225, 128, 0)

x, y = coordenadas 
R, G, B = (colores_rgb)

def CalculoNo(numero):
    Total_No = len(numero)
    
    print(f"maximo: {max(numero)} ")
    
    print(f"minimo: {min(numero)} ")
    
    print(f"promedio: {sum(numero) / len(Total_No):.2f}")
    return Total_No, max(numero), min(numero), sum(numero) / len(Total_No)


distancia = {
    ("Guate", "Esuintla"): 58,
    ("Guate", "Antigua"): 45,
}


