def cantidad_vocales_a(palabra):
    cant=0
    for x in range(len(palabra)):
        if palabra[x] == "a"or palabra[x] == "A":
            cant=cant+1
    return cant
# bloque principal
palabra=int(input("ingrese una palabra: "))
print("la palabra ", palabra,"tiene",cantidad_vocales_a(palabra), "a")