# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import sys

'''******************************MENU**********************************'''
class Menu:

    def __init__(self):
        self.elecciones = {
            "1": self.CargarArchivo,
            "2": self.GenerarGrafica,
            "3": self.quit
        }
    # END

    def mostrar_menu(self):
        print("""
        ************** PROYECTO 2 **************
        | Lenguajes Formales y de Programación |
        | Sección: A-, Canet: 201901816        |
        | Angel Oswaldo Arteaga García         |
        ****************************************

        ********** SIMPLE GRAPH MENU **+********
        1. Cargar Archivo
        2. Generar Gráfica
        3. Salir
        """)
    # END

    def run(self):
        while True:
            self.mostrar_menu()
            eleccion = input(">>Ingrese una opción:")
            accion = self.elecciones.get(eleccion)
            if accion:
                accion()
            else:
                print("No es una elección válida".format(eleccion))
    # END

    def CargarArchivo(self):
        print("Porfavor intruduzca la ubicación del archivo:")
    # END

    def GenerarGrafica(self):
        print('Porfavor ingrese la ruta del archivo primero.')
    # END

    def quit(self):
        print("Gracias por usar SimpleGraph...")
        sys.exit(0)
    # END

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    menu = Menu()
    menu.run()
# END

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
