def sumar(valor1, valor2):
    return valor1 + valor2

def resta(valor1, valor2):
    return valor1 - valor2

def multiplicacion(valor1, valor2):
    return valor1 * valor2

def division(valor1, valor2):
    try:
        return valor1 / valor2
    except ZeroDivisionError:
        print("No se puede dividir entre cero")
        return "operacion invalida"

try:
    valor1 = (int(input("Valor1: ")))
    valor2 = (int(input("Valor2: ")))
    operacion = input("Operacion: ")

    if (operacion=="suma"): 
        print("El resultado es: ", sumar(valor1, valor2))
    elif (operacion=="resta"):
        print("El resultado es: ", resta(valor1, valor2))
    elif (operacion=="multiplicacion"):
        print("El resultado es: ", multiplicacion(valor1, valor2))
    elif (operacion=="division"):
        print("El resultado es: ", division(valor1, valor2))
    else: 
        print("Operacion invalida")
except ValueError:
    print("Tipo de valores no permitidos")


