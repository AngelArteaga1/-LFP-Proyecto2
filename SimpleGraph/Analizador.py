import re
from Error import Error
from Token import Token
from Nodo import Nodo

class Analizador:

    def __init__(self, direccion):
        self.direccion = direccion


    '''******************************FUNCION_LEER_ARCHIVO**********************************'''
    def LeerArchivo(self):
        leido = False
        rutatxt = self.direccion
        if ".lfp" in rutatxt:
            try:
                archivo = open(rutatxt, "r")
                leido = True
                archivo.close()
            except:
                print("El archivo ingresado es incorrecto.\nPresione cualquier tecla para continuar")
                input()
        else:
            print("El archivo no es .lfp o es incorrecto.\nPresione cualquier tecla para continuar")
            input()
        if leido == True:
            print("VIvo")
            archivo = open(rutatxt, encoding="cp437", errors='ignore')
            lineas = archivo.readlines()
            archivo.close()
            argumento = ''
            for i in lineas:
                argumento = argumento+i
            AnalisisLexico(lineas)
    def GetNombreLista(self):
        return NombreLista
    def GetFormaLista(self):
        return FormaLista
    def GetEnlaceLista(self):
        return EnlaceLista
    def GetNombreDefault(self):
        return NombreDefaut
    def GetColorDefault(self):
        return ColorDefaut
    def GetNodosLista(self):
        return NodosLista
    def GetPerfecto(self):
        return Perfecto
    def GetErrores(self):
        return Errores
    def GetTokens(self):
        return Tokens

# VARIABLES GLOBALES
S = 0 # ESTADOS DE AUTOMATA
EC = 0 # Estado antes de que venga el comentario
TokenLexico = ''
# ALphabetos
Formas = ['circulo', 'rectangulo', 'triangulo', 'punto', 'hexagono', 'diamante'] # formas validas
Colores =  ['azul', 'azul2', 'azul3',
            'rojo', 'rojo2', 'rojo3',
            'amarillo', 'amarillo2', 'amarillo3',
            'anaranjado', 'anaranjado2', 'anaranjado3',
            'cafe', 'cafe2', 'cafe3',
            'gris', 'gris2', 'girs3',
            'morado', 'morado2', 'morado3',
            'verde', 'verde2', 'verde3',
            'blanco', '#'
           ] # colores validos
Boolean = ['verdadero', 'falso'] # posibles listas
Nodos = ['nodo', 'nodos'] # posibles entradas de nodos

Errores = []
Tokens = []
Perfecto = True
Identificador = ''
Index = 0
# Atributos de la lista
NombreLista = ''
FormaLista = ''
EnlaceLista = ''
NombreDefaut = ''
ColorDefaut = ''
# Atributos de los nodos
CantidadNodo = ''
NombreNodo = ''
ColorNodo = ''
# Lista de Nodos
NodosLista = []



def AnalisisLexico(lineas):
    # Variables
    global S
    global TokenLexico
    global Errores
    global Tokens
    global Perfecto
    global Identificador
    global EC
    global Index
    # Atributos de la lista
    global NombreLista
    global FormaLista
    global EnlaceLista
    global NombreDefaut
    global ColorDefaut
    # Atributos del nodo
    global CantidadNodo
    global NombreNodo
    global ColorNodo
    # Lista de nodos
    global NodosLista

    # Reseate todo WACHO
    S = 0  # ESTADOS DE AUTOMATA
    EC = 0  # Estado antes de que venga el comentario
    TokenLexico = ''
    Errores = []
    Tokens = []
    Perfecto = True
    Identificador = ''
    Index = 0
    # Atributos de la lista
    NombreLista = ''
    FormaLista = ''
    EnlaceLista = ''
    NombreDefaut = ''
    ColorDefaut = ''
    # Atributos de los nodos
    CantidadNodo = ''
    NombreNodo = ''
    ColorNodo = ''
    # Lista de Nodos
    NodosLista = []

    contador = 0
    # Quitarle los tabuladores y saltos a cada linea
    for i in lineas:
        lineas[contador] = re.sub('[\t]', ' ', lineas[contador])
        lineas[contador] = re.sub('[\n]', '', lineas[contador])
        contador = contador + 1
    # ANALISI LEXICO TURBIO
    contador = 1
    for i in lineas:
        AutomataGeneral(i, contador)
        contador = contador + 1
    contador = 1
    for i in Errores:
        print('Error No: ' + str(contador) + ' | Linea: ' + str(i.GetLinea()) + ' | Columna: ' + str(i.GetColumna()) + ' | Descripcion: ' + str(i.GetDescripcion()))
        contador = contador + 1
    print("***************************TOKENS********************************")
    contador = 1
    for i in Tokens:
        print('Token No: ' + str(contador) + ' | Linea: ' + str(i.GetLinea()) + ' | Columna: ' + str(i.GetColumna()) + ' | Lexema: ' + str(i.GetLexema()) + ' | Token: ' + str(i.GetToken()))
        contador = contador + 1
    if (S == 0 and Perfecto == True):
        print('Proceso teminado! El archivo es perfeto :)')
    else:
        print('Proceso teminado! El archivo tiene erorres :(')
        print('Porfavor genera la gráfica para ver la tabla de errores...')
    print('Oprima cualquier letra para continuar.')
    # END

def AutomataGeneral(lineas, fila):
    global S
    global TokenLexico
    global Errores
    global Tokens
    global Perfecto
    global Identificador
    global EC
    global Index
    # Atributos de la lista
    global NombreLista
    global FormaLista
    global EnlaceLista
    global NombreDefaut
    global ColorDefaut
    # Atributos del nodo
    global CantidadNodo
    global NombreNodo
    global ColorNodo
    # Lista de nodos
    global NodosLista

    columna = 1  # Columnas del analizador
    for i in lineas:
        '''******************************COMENTARIOS*******************************'''
        #ESTADO 1000
        if S == 1000:
            if i == '/':
                S = 1001
            else:
                #Error
                print("error, estado: " + str(S) + 'Fila: ' + str(fila) + ' Columna: ' + str(columna) + ' i: ' + i)
                Perfecto = False
        # ESTADO 1001
        elif S == 1001:
            if columna == len(lineas):
                S = EC
        # **************************ERRORES DE LISTAS*********************************
        #ESTADO -1
        elif S == -1:
            TokenLexico = ''
            if i == '{':
                S = 11
            elif i == '/':
                EC = S
                S = 1000
        #ESTADO -2
        elif S == -2:
            TokenLexico = ''
            if i == ';':
                S = 21
            elif i == '/':
                EC = S
                S = 1000
        #ESTADO -3
        elif S == -3:
            TokenLexico = ''
            if i == ';':
                S = 0
            elif i == '/':
                EC = S
                S = 1000
        # **************************ESTADOS DE LISTAS*********************************
        #ESTADO 0
        elif S == 0:
            if i.isalpha():
                Index = columna
                S = 1
                TokenLexico = TokenLexico + i
            elif i == ' ':
                S = 0
            elif i == '/':
                EC = S
                S = 1000
            else:
                Perfecto = False
                error = Error(fila, columna, 'Caracter desconocido: ' + i)
                Errores.append(error)
                TokenLexico = ''
        #ESTADO 1
        elif S == 1:
            if i.isalpha():
                S = 1
                TokenLexico = TokenLexico + i
            elif i == '(' and TokenLexico.lower() == 'lista':
                token = Token(fila,columna, TokenLexico, 'ListaTk')
                Tokens.append(token)
                token = Token(fila, columna, i, 'ParATk')
                Tokens.append(token)
                TokenLexico = ""
                S = 2
            elif i == ' ':
                S = 1
            else:
                Perfecto = False
                error = Error(fila, Index, 'No se esperaba: ' + TokenLexico)
                Errores.append(error)
                TokenLexico = ""
                S = -1
        #ESTADO 2
        elif S == 2:
            if i == "'":
                S = 3
            elif i == ' ':
                S = 2
            else:
                Perfecto = False
                error = Error(fila, columna, 'Caracter desconocido: ' + i)
                Errores.append(error)
                S = -1
        #ESTADO 3
        elif S == 3:
            if i == ' ':
                S = 3
            elif i != "'":
                S = 4
                Identificador = Identificador + i
            else:
                Perfecto = False
                S = 5
        #ESTADO 4
        elif S == 4:
            if i == ' ':
                S = 4
            elif i != "'":
                S = 4
                Identificador = Identificador + i
            elif i == "'":
                NombreLista = Identificador
                token = Token(fila, columna, Identificador, 'IdTK')
                Tokens.append(token)
                Identificador = ''
                S = 5
        #ESTADO 5
        elif S == 5:
            if i == ' ':
                S = 5
            elif i == ',':
                S = 6
                token = Token(fila, columna, i, 'ComaTk')
                Tokens.append(token)
            else:
                Perfecto = False
                error = Error(fila, columna, 'No se esperaba: ' + i)
                Errores.append(error)
                S = -1
        #ESTADO 6
        elif S == 6:
            if i.isalpha():
                Index = columna
                S = 7
                TokenLexico = TokenLexico + i
            elif i == " ":
                S = 6
            else:
                Perfecto = False
                error = Error(fila, columna, 'Caracter desconocido: ' + i)
                Errores.append(error)
                TokenLexico = ''
                S = -1
        #ESTADO 7
        elif S == 7:
            if i.isalpha():
                S = 7
                TokenLexico = TokenLexico + i
            elif i == ',' and TokenLexico.lower() in Formas:
                FormaLista = TokenLexico
                token = Token(fila, columna, TokenLexico, 'FormaTk')
                Tokens.append(token)
                token = Token(fila, columna, i, 'ComaTk')
                Tokens.append(token)
                S = 8
                TokenLexico = ''
            elif i == ' ':
                S = 7
            else:
                Perfecto = False
                error = Error(fila, Index, 'No se esperaba: ' + TokenLexico)
                Errores.append(error)
                TokenLexico = ''
                S = -1
        #ESTADO 8
        elif S == 8:
            if i.isalpha():
                Index = columna
                TokenLexico = TokenLexico + i
                S = 9
            elif i == ' ':
                S = 8
            else:
                Perfecto = False
                error = Error(fila, columna, 'Caracter desconocido: ' + i)
                Errores.append(error)
                TokenLexico = ''
                S = -1
        #ESTADO 9
        elif S == 9:
            if i.isalpha():
                TokenLexico = TokenLexico + i
                S = 9
            elif i == ')' and TokenLexico.lower() in Boolean:
                EnlaceLista = TokenLexico
                token = Token(fila, columna, TokenLexico, 'BooleanTK')
                Tokens.append(token)
                token = Token(fila, columna, i, 'ParCTk')
                Tokens.append(token)
                TokenLexico = ''
                S = 10
            elif i == ' ':
                S = 9
            else:
                Perfecto = False
                error = Error(fila, Index, 'No se esperaba: ' + TokenLexico)
                Errores.append(error)
                TokenLexico = ''
                S = -1
        #ESTADO 10
        elif S == 10:
            if i == '{':
                S = 11
                token = Token(fila, columna, i, 'CorATk')
                Tokens.append(token)
            elif i == ' ':
                S = 10
            else:
                Perfecto = False
                error = Error(fila, columna, 'Caracter desconocido: ' + i)
                Errores.append(error)
                S = 11
        #ESTADO 11
        elif S == 11:
            if i.isalpha():
                Index = columna
                TokenLexico = TokenLexico + i
                S = 12
            elif i == ' ':
                S = 11
            else:
                Perfecto = False
                error = Error(fila, columna, 'Caracter desconocido: ' + i)
                Errores.append(error)
                TokenLexico = ''
                S = -2
        #ESTADO 12
        elif S == 12:
            if i.isalpha():
                TokenLexico = TokenLexico + i
                S = 12
            elif i == "(" and TokenLexico.lower() in Nodos:
                token = Token(fila, columna, TokenLexico, 'NodoTk')
                Tokens.append(token)
                token = Token(fila, columna, i, 'ParATk')
                Tokens.append(token)
                S = 13
                TokenLexico = ''
            elif i == ' ':
                S = 12
            else:
                Perfecto = False
                error = Error(fila, Index, 'No se esperaba: ' + TokenLexico)
                Errores.append(error)
                TokenLexico = ''
                S = -2
        #ESTADO 13
        elif S == 13:
            if i.isdigit():
                CantidadNodo = CantidadNodo + i
                S = 14
            elif i == "'":
                S = 16
            elif i == '#':
                NombreNodo = i
                S = 18
                token = Token(fila, columna, i, 'NumeralTk')
                Tokens.append(token)
            elif i == ' ':
                S = 13
            else:
                Perfecto = False
                error = Error(fila, columna, 'No se esperaba: ' + i)
                Errores.append(error)
                S = -2
        #ESTADO 14
        elif S == 14:
            if i.isdigit():
                CantidadNodo = CantidadNodo + 1
                S = 14
            elif i == ',':
                token = Token(fila, columna, CantidadNodo, 'NumTk')
                Tokens.append(token)
                token = Token(fila, columna, i, 'ParATk')
                Tokens.append(token)
                S = 15
            elif i == ' ':
                S = 13
            else:
                Perfecto = False
                error = Error(fila, columna, 'No se esperaba: ' + i)
                Errores.append(error)
                S = -2
        #ESTADO 15
        elif S == 15:
            if i == "'":
                S = 16
            elif i == '#':
                S = 18
                token = Token(fila, columna, i, 'NumeralTk')
                Tokens.append(token)
            elif i == ' ':
                S = 15
            else:
                Perfecto = False
                error = Error(fila, columna, 'No se esperaba: ' + i)
                Errores.append(error)
                S = -2
        #ESTADO 16
        elif S == 16:
            if i != "'":
                S = 17
                Identificador = Identificador + i
            else:
                S = 18
        #ESTADO 17
        elif S == 17:
            if i != "'":
                Identificador = Identificador + i
                S = 17
            else:
                NombreNodo = Identificador
                token = Token(fila, columna, Identificador, 'IdTk')
                Tokens.append(token)
                Identificador = ''
                S = 18
        #ESTADO 18
        elif S == 18:
            if i == ")":
                S = 19
                token = Token(fila, columna, i, 'ParATk')
                Tokens.append(token)
            elif i == ' ':
                S = 18
            else:
                Perfecto = False
                error = Error(fila, columna, 'No se esperaba: ' + i)
                Errores.append(error)
                S = -2
        #ESTADO 19
        elif S == 19:
            if i.isalpha():
                TokenLexico = i
                Index = columna
                S = 20
            elif i == '#':
                TokenLexico = i
                S = 20
            elif i == ' ':
                S = 19
            else:
                Perfecto = False
                error = Error(fila, columna, 'Caracter desconocido: ' + i)
                Errores.append(error)
                S = -2
        #ESTADO 20
        elif S == 20:
            if i.isalnum():
                TokenLexico = TokenLexico + i
                S = 20
            elif i == ';' and TokenLexico.lower() in Colores:
                token = Token(fila, columna, TokenLexico, 'ColorTK')
                Tokens.append(token)
                token = Token(fila, columna, i, 'PuntoComaTk')
                Tokens.append(token)
                # crear el nodo
                ColorNodo = TokenLexico
                nodo = Nodo(NombreNodo, ColorNodo, CantidadNodo)
                NodosLista.append(nodo)
                # Resetear todo
                ColorNodo = ''
                NombreNodo = ''
                CantidadNodo = ''
                # Cambio de estado
                TokenLexico = ''
                S = 21
            elif i == ' ':
                S = 20
            else:
                print('pedro')
                Perfecto = False
                error = Error(fila, Index, 'No se esperaba: ' + TokenLexico)
                Errores.append(error)
                S = 21
        #ESTADO 21
        elif S == 21:
            if i.isalnum():
                Index = columna
                TokenLexico = TokenLexico + i
                S = 11
            elif i == '}':
                token = Token(fila, columna, i, 'CorCTk')
                Tokens.append(token)
                S = 22
            elif i == ' ':
                S = 21
            elif i == '/':
                token = Token(fila, columna, '//', 'ComentarioTk')
                Tokens.append(token)
                EC = S
                S = 1000
            else:
                Perfecto = False
                TokenLexico = ''
                #ERROR ESPECIAL NO MANEJADO
                error = Error(fila, columna, 'No se esperaba: ' + i)
                Errores.append(error)
        #ESTADO 22
        elif S == 22:
            if i.isalpha():
                TokenLexico = TokenLexico + i
                Index = columna
                S = 23
            elif i == ' ':
                S = 22
            else:
                Perfecto = False
                error = Error(fila, columna, 'Caracter desconocido: ' + i)
                Errores.append(error)
                S = -3
        #ESTADO 23
        elif S == 23:
            if i.isalpha():
                TokenLexico = TokenLexico + i
                S = 23
            elif i == '(':
                token = Token(fila, columna, TokenLexico, 'DefectoTk')
                Tokens.append(token)
                token = Token(fila, columna, i, 'ParATk')
                Tokens.append(token)
                TokenLexico = ''
                S = 24
            elif i == ' ':
                S = 23
            else:
                Perfecto = False
                error = Error(fila, Index, 'No se esperaba: ' + TokenLexico)
                Errores.append(error)
                S = -3
        #ESTADO 24
        elif S == 24:
            if i == "'":
                S = 25
            elif i == ' ':
                S = 24
            else:
                Perfecto = False
                error = Error(fila, columna, 'No se esperaba: ' + i)
                Errores.append(error)
                S = -3
        #ESTADO 25
        elif S == 25:
            if i != "'":
                S = 26
                Identificador = Identificador + i
            else:
                S = 27
        #ESTADO 26
        elif S == 26:
            if i != "'":
                S = 26
                Identificador = Identificador + i
            else:
                NombreDefaut = Identificador
                token = Token(fila, columna, Identificador, 'IdTk')
                Tokens.append(token)
                Identificador = ''
                S = 27
        #ESTADO 27
        elif S == 27:
            if i == ')':
                S = 28
                token = Token(fila, columna, i, 'ParCierraTk')
                Tokens.append(token)
            elif i == ' ':
                S = 27
            else:
                Perfecto = False
                error = Error(fila, columna, 'No se esperaba: ' + i)
                Errores.append(error)
                S = -3
        #ESTADO 28
        elif S == 28:
            if i.isalnum():
                Index = columna
                TokenLexico = TokenLexico + i
                S = 29
            elif i == ' ':
                S = 28
            else:
                Perfecto = False
                error = Error(fila, columna, 'Caracter desconocido: ' + i)
                Errores.append(error)
                S = -3
                TokenLexico = ''
        #ESTADO 29
        elif S == 29:
            if i.isalnum():
                TokenLexico = TokenLexico + i
                S = 29
            elif i == ';' and TokenLexico.lower() in Colores:
                token = Token(fila, columna, TokenLexico, 'ColorTk')
                Tokens.append(token)
                token = Token(fila, columna, i, 'PuntoComaTk')
                Tokens.append(token)
                # definir el color
                ColorDefaut = TokenLexico
                TokenLexico = ''
                S = 0
            elif i == ' ':
                S = 29
            else:
                Perfecto = False
                error = Error(fila, Index, 'No se esperaba: ' + TokenLexico)
                Errores.append(error)
                TokenLexico = ''
                S = -3
        # print('estado: ' + str(S) + '  |' + str(fila) + '|' + str(columna) + '| i: ' + i)
        columna = columna + 1
