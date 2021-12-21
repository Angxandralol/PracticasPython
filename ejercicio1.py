#Una empresa que trabaja con vehículos desea calcular las necesidades 
# de combustible (cantidad de combustible necesario para llenar 
# los depósitos de todos sus vehículos) para lo cual nos han facilitado este esquema de cálculo. 
# Se desea crear un programa para que puedan realizar el cálculo de forma automatizada.
# Turismos, Todoterrenos, Capturismos, Captodot
# Necesidadescom = Turismos * Capturismos + Todoterrenos * Captodot
 
# VARIABLES 
turismos = input("Ingrese cantidad de autos turismos: ") #lo que ingrese el usuario de tipo str
turismos = int(turismos) #por eso se debe convertir a un entero
todoterrenos = input("Ingrese cantidad de autos todoterrenos: ")
todoterrenos = int(todoterrenos)
capturismos = input("Ingrese cantidad de capturismos: ")
capturismos = int(capturismos)
captodot = input("Ingrese cantidad de captodot: ")
captodot = int(captodot)

def calculoNecesidadesCombustible(turismos, todoterrenos, capturismos, captodot):
    necesidadesCom = turismos * capturismos + todoterrenos * captodot
    return necesidadesCom

resultado = calculoNecesidadesCombustible(turismos, todoterrenos, capturismos, captodot)
print("La cantidad de combustible necesario es: ", resultado)