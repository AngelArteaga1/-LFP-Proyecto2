class Token:
    def __init__(self, linea, columna, lexema, token):
        self.linea = linea
        self.columna = columna
        self.lexema = lexema
        self.token = token

    '''******************************FUNCIONES/GET/SET**********************************'''

    def GetLinea(self):
        return self.linea
    # END
    def GetColumna(self):
        return self.columna
    # END
    def GetLexema(self):
        return self.lexema
    # END
    def GetToken(self):
        return self.token
    # END