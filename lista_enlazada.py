# Eithner Geovanny Palacios Palacios
# Sistemas de control de versiones - 37

class Nodo:
    def __init__(self):
        self.dato = None
        self.siguiente = None

class lista_enlazada:
    def __init__(self):
        self.cabeza = None

    def vaciar(self):
        return self.cabeza is None
    
    