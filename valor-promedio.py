def retornar_promedio(v1, v2,v3):
    promedio=(v1 + v2 + v3) //3
    return promedio
# bloque principal
valor1=int(input("ingrese primer valor:"))
valor2=int(input("ingrese segundo valor:"))
valor3=int(input("ingrese tercer valor:"))
print("valor promedio de los tres numeros es:")
print(retornar_promedio(valor1, valor2, valor3))