print("WHILE: ")
print("\n")

contador = 0
while (contador < 3):
    contador += 1
    print(contador)

print("\n")

contador = 0
while (contador < 4):
    contador += 1
    print(contador)
    if (contador == 3): break

print("\n")

contador = 0
while ((contador%2)==0):
    contador += 1
else: print("Contador no es menor que 4")

print("\n")

contador = 0
print("Conteo sin el 5: ")
while (contador < 6): 
    contador += 1
    if (contador == 5): continue
    print(contador)
print("\n")

print("FOR: ")
print("\n")

lista = [1,2,3,4,5]
 
for palabra in range(len(lista)):
    print ("El número: {0}, está en en el índice: {1}".format(
        lista[palabra], palabra))
print("\n")

print("La i va incrementando por cada elemento de la lista:")
for i in range(len(lista)):
    print(i)