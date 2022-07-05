def retornar_perimetro(lado):
    perimetro = lado*4
    return perimetro
# bloque principal
lado=int(input("ingrese el lado del cuadrado:"))
print("el perimetro del cuadrado es", retornar_perimetro(lado))