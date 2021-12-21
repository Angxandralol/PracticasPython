class Coche():
    def __init__(self): #<----Constructor
        self.__largo = 250
        self.__ancho = 120
        self.__ruedas = 4
        self.__marcha = False
    
    def arrancar(self, arrancamos):
        self.__marcha = arrancamos
        if (self.__chequeo_interno()==True and self.__marcha):
            return print("El carro está en marcha")
        else: print("El carro no está en marcha")
    
    def __chequeo_interno(self):
        print("Relizando chequeo interno")
        self.gasolina = "ok"
        self.aceite = "ok"
        self.puertas = "cerradas"

        if (self.gasolina == "ok" and self.aceite == "ok" and self.puertas == "cerradas"):
            return True
        else: return False

miCoche = Coche() 
miCoche.arrancar(True)


