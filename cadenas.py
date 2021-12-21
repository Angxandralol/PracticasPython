cadenaCorta = "Hola"
cadenaLarga = """Hola, me llamo Angyee
Esta cadena permite salto de lineas"""

print(cadenaCorta)
print(cadenaLarga)
print("\n")

longitudCadena = len(cadenaCorta)
print("La longitud de la cadena es:", longitudCadena)
longitudCadena = len(cadenaLarga)
print("La longitud de la cadena es:", longitudCadena) #Cuenta espacios y comas
print("\n")

print(cadenaCorta[0])
print(cadenaCorta[3])
print(cadenaCorta[1:3])
print("\n")

print("angyee" in cadenaLarga)
print("Angyee" in cadenaLarga)
print("\n")