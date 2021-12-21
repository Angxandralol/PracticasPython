def suma(num1,num2):
    print(num1 + num2)

suma(5,7)
#################################################
def resta(num1,num2):
    result = num1 - num2
    return result

print(resta(10,4))
########
# Paso por referencia

def cambiaNumero(numeroOriginal):
    return numeroOriginal*2

numeroOriginal = 10
numeroOriginal = cambiaNumero(numeroOriginal)

print(numeroOriginal)
#############################

