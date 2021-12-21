#Key,Value
diccionario1 = {
    "clave1": 243,
    "clave2": True,
    "clave3": "Pepito", 
    "clave4": [1,2,3,4]
}

print(diccionario1)
print(diccionario1["clave1"])
print("\n")

versiones = dict(android=1, apple=2, windows=3, linux=None)
print(versiones["android"])
print("\n")

versiones["linux"] = 4
print(versiones)
print("\n")

print("android" in versiones)
print("mac" in versiones)
print("\n")

diccionario1.clear()
print(diccionario1)
print("\n")

otro_versiones = versiones.copy()
print("Copia: ",otro_versiones)
print(otro_versiones["android"])
print("\n")

secuencia = ("perro", "gato", "loro")
animales = dict.fromkeys(secuencia)
print(animales)
animales.clear()
animales = dict.fromkeys(secuencia, 1)
print(animales)
print("\n")

print(animales.get("loro"))
print(animales.get("pez"))
print("\n")

print(versiones.items())
print("\n")

#Hay muchos más métodos...



