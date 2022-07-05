def retornar_superficie(lado1, lado2):
    superficie=lado1*lado2
    return superficie
# bloque principal
print("primer rectangulo")
lado1=int(input("ingrese lado menor del rectangulo:"))
lado2=int(input("ingrese lado mayor del rectangulo:"))
print("segundo rectangulo")
lado3=int(input("ingrese lado menor del rectangulo:"))
lado4=int(input("ingrese lado mayor del rectangulo"))
if retornar_superficie(lado1,lado2)== retornar_superficie(lado3,lado4):
    print("los dos rectangulos tienen la misma superficie")
else:
    print("el segundo rectangulos tiene una superficie mayor")