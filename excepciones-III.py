def evaluarEdad(edad):

    if (edad<=0):
        raise TypeError("Edad inválida")

    if ((edad>=1) and (edad<3)):
        return "Tu eres un bebé"
    elif (edad<12):
        return "Tu eres un niño/a"
    elif (edad<18):
        return "Tu eres un adolescente"
    elif (edad<40):
        return "Tu eres adulto"
    elif (edad<60):
        return "Tu eres adulto mayor"
    elif (edad<110):
         return "Tu eres viejo"
    else:
        return "Dudo que mucho que hayas colocado tu edad real"

edad = (int(input("Ingrese su edad: ")))
print(evaluarEdad(edad))