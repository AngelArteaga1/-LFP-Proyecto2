class Nodo:
    def __init__(self, nombre, color, cantidad):
        self.nombre = nombre
        self.color = color
        self.cantidad = cantidad

    '''******************************FUNCIONES/GET/SET**********************************'''
    def GetNombre(self):
        return self.nombre
    # END
    def GetColor(self):
        return self.color
    # END
    def GetCantidad(self):
        return self.cantidad
    # END