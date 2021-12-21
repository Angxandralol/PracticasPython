
def divide():
    try: 
        valor1=(float(input("Primer Numero: ")))
        valor2=(float(input("Segundo Numero: ")))
        print("Division: ", valor1/valor2)
    except ValueError: 
        print("Tipo de valores invalidos")
    except ZeroDivisionError:
        print("NO se puede dividir entre cero")



def divide1():
    try: 
        valor1=(float(input("Primer Numero: ")))
        valor2=(float(input("Segundo Numero: ")))
        print("Division: ", valor1/valor2)
    except:
        print("Ha ocurrido un error")

def divide2():
    try: 
        valor1=(float(input("Primer Numero: ")))
        valor2=(float(input("Segundo Numero: ")))
        print("Division: ", valor1/valor2)
    finally: 
        print("Esto siempre se ejecutará")

######LLAMADA#####
divide()
