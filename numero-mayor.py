def retorne_mayor(v1, v2):
    if v1 > v2:
        mayor = v1
    else:
        mayor = 2
    return mayor
# bloque pricipal
valor1 =int(input("ingrese el primer valor:"))
valor2=int(input("ingrese el segundo valor:"))
print("el numero mayor es :", retorne_mayor(valor1,valor2))


