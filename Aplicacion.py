from Analizador import Analizador
from Graficador import Graficador
a = Analizador()
#El flujo del Programa
class Aplicacion:
    def __init__(self):
        self.app()

    def app(self):
        while True:
            res = input('''
1. Cargar Data
2. Cargar Instrucciones
3. Analizar
4. Reportes
5. Salir
Selecciona una opcion: ''')
            #switch
            if res == '1':
                a.Leer('.data')
                a.Analizar_1()
            elif res == '2':
                a.Leer('.lfp')
                a.Analizar_2()
            elif res == '3':
                res2 = int(a.getData())
                instr = a.getInstr(res2)
                nombre = instr['nombre']
                grafica = instr['grafica']
                titulo = instr['titulo']
                titulox = instr['titulox']
                tituloy = instr['tituloy']
                ejex = a.EjeX(res2)
                ejey = a.EjeY(res2)
                c = Graficador(nombre, grafica, titulo, titulox, tituloy, ejex, ejey)
                c.Analizar()

            elif res == '4':
                pass
            elif res == '5':
                print("Adios")
                break
            else:
                print("Por favor seleccione un opcion valida")

b = Aplicacion()