from typing import OrderedDict


lista1 = [1,2,3,4,5,6,7,8]
print(lista1)
print(lista1[3])
print(lista1[2:5])
print("\n")

lista2 = ["Hola", 22.3, "o", 5, False]
print(lista2)
print("\n")

lista3 = [] #Inicialización de una lista vacía
lista3.append(11)
lista3.append(13)
lista3.append(3534)
print(lista3)
print("\n")

lista4 = [2,3,4,534,3,34,42,1,2,3,4,3,5]
print(lista4)
print("Cantidad de veces que el 3 está en esta lista4:", lista4.count(3))
print("\n")

lista5 = [1,2,3]
print(lista5)
lista5.extend([4,5,6,7,8,9])
print(lista5)
lista5.extend(range(10,21))
print(lista5)
print("\n")

print(lista5.index(12))
print("\n")

lista3.insert(2, 33)
print(lista3)
print("\n")

ultimoElemento = lista3.pop()
print(lista3)
print("Elemento borrado: ", ultimoElemento)
lista3.pop(0)
print(lista3)
print("\n")

lista4.remove(2)
print("El primer dos ha sido borrado con éxito de la lista4: ", lista4)
print("\n")

lista5.reverse()
print(lista5)
print("\n")

lista4.sort()
print(lista4)
lista4.sort(reverse=True)
print(lista4)
print("\n")