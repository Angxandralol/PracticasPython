def generadorNumerosPares(contador):
    while (contador < 10): 
        contador+=1
        if ((contador%2)==0): yield contador

numero = generadorNumerosPares(0)
print(next(numero))
print(next(numero))
print(next(numero))
print(next(numero))

print("\n")

lista1 = [1,2,3,4,5,6]
lista_iterable = iter(lista1)
print(next(lista_iterable))
print(next(lista_iterable))
print(next(lista_iterable))
print(next(lista_iterable))

print("\n")

lista2 = ["Hola", "como estas", "?"]

def palabras(lista2):
    for elemento in lista2:
        yield elemento
    
def letras(lista2):
    for elemento in lista2:
        yield from elemento #el yield from se encarga de entrar a los subelementos del elemento. En este caso, las letras de la palabra de la lista2

palabra = palabras(lista2)
letra = letras(lista2)

print(next(palabra))
print(next(letra))
print(next(letra))
print(next(letra))
print(next(letra))