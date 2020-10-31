class Error:
    def __init__(self, linea, columna, descripcion):
        self.linea = linea
        self.columna = columna
        self.descripcion = descripcion

    '''******************************FUNCIONES/GET/SET**********************************'''
    def GetLinea(self):
        return self.linea
    # END
    def GetColumna(self):
        return self.columna
    # END
    def GetDescripcion(self):
        return self.descripcion
    # END