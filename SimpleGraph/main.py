# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import sys
from Analizador import Analizador

# VARIABLES GLOBALES
analizador = None

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
        global analizador
        analizador = Analizador(input())
        analizador.LeerArchivo()
        input()
    # END

    def GenerarGrafica(self):
        if analizador ==  None:
            print('Porfavor ingrese la ruta del archivo primero.')
        else:
            GraficarReporte()
    # END

    def quit(self):
        print("Gracias por usar SimpleGraph...")
        sys.exit(0)
    # END

def Forma(forma):
    forma = forma.lower()
    resultado = ''
    if forma == 'circulo':
        resultado = 'circle'
    elif forma == 'rectangulo':
        resultado = 'rect'
    elif forma == 'triangulo':
        resultado = 'triangle'
    elif forma == 'punto':
        resultado = 'point'
    elif forma == 'hexagono':
        resultado = 'hexagon'
    elif forma == 'diamante':
        resultado = 'diamond'
    return resultado

def Color(color):
    color = color.lower()
    resultado = ''
    if color == 'azul':
        resultado = 'blue'
    elif color == 'azul2':
        resultado = 'blue2'
    elif color == 'azul3':
        resultado = 'blue3'
    elif color == 'rojo':
        resultado = 'red'
    elif color == 'rojo2':
        resultado = 'red2'
    elif color == 'rojo3':
        resultado = 'red3'
    elif color == 'amarillo':
        resultado = 'yellow'
    elif color == 'amarillo2':
        resultado = 'yellow2'
    elif color == 'amarillo3':
        resultado = 'yellow3'
    elif color == 'anaranjado':
        resultado = 'orangered'
    elif color == 'anaranjado2':
        resultado = 'orangered2'
    elif color == 'anaranjado3':
        resultado = 'orangered3'
    elif color == 'cafe':
        resultado = 'brown'
    elif color == 'cafe2':
        resultado = 'brown2'
    elif color == 'cafe3':
        resultado = 'brown3'
    elif color == 'gris':
        resultado = 'gray'
    elif color == 'gris2':
        resultado = 'gray41'
    elif color == 'gris3':
        resultado = 'gray66'
    elif color == 'morado':
        resultado = 'purple'
    elif color == 'morado2':
        resultado = 'purple2'
    elif color == 'morado3':
        resultado = 'purple3'
    elif color == 'verde':
        resultado = 'green'
    elif color == 'verde2':
        resultado = 'green2'
    elif color == 'verde3':
        resultado = 'green3'
    elif color == 'blanco':
        resultado = 'white'
    elif color == '#':
        resultado = '#'
    return resultado

def GraficarReporte():
    file = open('Reporte.html', 'w', encoding="cp437", errors='ignore')
    file.write('<!doctype html>\n')
    file.write('<html>\n')
    file.write('<head>\n<meta charset="utf-8">\n<title>Reporte</title>\n</head>\n<style>\n.center{\ntext-align: center;\n}\n</style>\n')

    file.write('<body>\n')
    file.write('<div class="center">\n')
    if analizador.GetPerfecto() == True:
        GraficarLista()
        file.write('<h1>Grafica de la Lista</h1>\n')
        file.write('<img src="borrar-fondo-imagen.webp" alt="">\n')
    else:
        # Crear tabla de errores
        errores = analizador.GetErrores()
        contador = 1
        file.write('<h1>Tabla de errores</h1>\n')
        file.write('<table border="1" style="margin: 0 auto;">\n')
        for i in errores:
            file.write('<tr>\n')
            file.write('<td>' + str(contador) + '</td>\n')
            file.write('<td>' + str(i.GetLinea()) + '</td>\n')
            file.write('<td>' + str(i.GetColumna()) + '</td>\n')
            file.write('<td>' + str(i.GetDescripcion()) + '</td>\n')
            file.write('</tr>\n')
            contador = contador + 1
        file.write('</table>\n')

    # Tabla de tokens
    file.write('<h1>Tabla de tokens</h1>\n')
    file.write('<table border="1" style="margin: 0 auto;">\n')
    tokens = analizador.GetTokens()
    contador = 1
    for i in tokens:
        file.write('<tr>\n')
        file.write('<td>' + str(contador) + '</td>\n')
        file.write('<td>' + str(i.GetLinea()) + '</td>\n')
        file.write('<td>' + str(i.GetColumna()) + '</td>\n')
        file.write('<td>' + str(i.GetLexema()) + '</td>\n')
        file.write('<td>' + str(i.GetToken()) + '</td>\n')
        file.write('</tr>\n')
        contador = contador + 1
    file.write('</table>\n')

    file.write('</div>\n')
    file.write('</body>\n')
    file.write('</html>\n')

def GraficarLista():
    # Elementos de lista
    NombreLista = analizador.GetNombreLista()
    FormaLista = Forma(analizador.GetFormaLista())
    EnlaceLista = analizador.GetEnlaceLista()
    ColorDefault = Color(analizador.GetColorDefault())
    NombreDefault = analizador.GetNombreDefault()

    # Obtener los nodos
    Nodos = analizador.GetNodosLista()
    for i in Nodos:
        print(i.GetColor())
        print(i.GetNombre())
    #Empezar a graficar
    file = open('Grafica.dot', 'w', encoding="cp437", errors='ignore')
    file.write('digraph Grafica{\n')
    file.write('node[shape="'+ FormaLista +'", fillcolor="'+ ColorDefault +'", style=filled, label="'+ NombreDefault +'"]\n')
    Lista = []
    Contador = 1
    for i in Nodos:
        Nombre = i.GetNombre()
        color = Color(i.GetColor())
        Cantidad = i.GetCantidad()
        tortilla = 0
        if Cantidad == '':
            tortilla = 1
        else:
            tortilla = int(Cantidad)
        # creando los nodos
        for j in range(tortilla):
            if Nombre != '#' and color != '#':
                file.write('N' + str(Contador) + ' [label="' + Nombre + '", fillcolor="' + color + '"]\n')
            elif Nombre == '#' and color != '#':
                file.write('N' + str(Contador) + ' [fillcolor="' + color + '"]\n')
            elif color == '#' and Nombre != '#':
                file.write('N' + str(Contador) + ' [label="' + Nombre + '"]\n')
            elif color == '#' and Nombre == '#':
                file.write('N' + str(Contador) + '\n')
            Lista.append('N' + str(Contador))
            Contador = Contador + 1
    file.write('rankdir="LR";\nlabelloc="t";\nlabel="' + NombreLista + '";\nfontsize=24;\n')
    # Realizando los enlaces
    Contador = 1
    for i in Lista:
        if i == Lista[-1]:
            file.write(i + '\n')
        else:
            file.write(i + '->')
    if EnlaceLista.lower() == 'verdadero':
        Lista = Lista[::-1]
        for i in Lista:
            if i == Lista[-1]:
                file.write(i + '\n')
            else:
                file.write(i + '->')
    file.write('}')
    file.close()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    menu = Menu()
    menu.run()
# END

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
