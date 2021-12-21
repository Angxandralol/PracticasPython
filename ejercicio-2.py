import math

def calculoRaizCuadrada(numero): 
    if numero<0:
        raise ValueError("El numero no puede ser negativo")    
    else:
        return math.sqrt(numero)

numero = (int(input("Ingresa un numero: ")))  

try:
    print(calculoRaizCuadrada(numero))
except ValueError as ErrorNumeroNegativos:
    print(ErrorNumeroNegativos)

print("end")