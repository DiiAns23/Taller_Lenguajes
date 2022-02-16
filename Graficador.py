import matplotlib.pyplot as grafiquita

class Graficador:

    def __init__(self, nombre, grafica, titulo = "", titulox = "", tituloy = "", ejex = [], ejey = []):
        self.nombre = nombre
        self.grafica = grafica
        self.titulo = titulo
        self.titulox = titulox
        self.tituloy = tituloy
        self.ejex = ejex
        self.ejey = ejey

    def Analizar(self):
        #Se crea la grafica
        grafiquita.bar(self.ejex, self.ejey) # ["producto 1", "producto 2", "producto 3"], [30,23,45]
        #Label X
        grafiquita.xlabel(self.titulox)

        #Label y
        grafiquita.ylabel(self.tituloy)

        #Titulo
        grafiquita.title(self.titulo)
        grafiquita.show()

        