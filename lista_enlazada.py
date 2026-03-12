# Eithner Geovanny Palacios Palacios
# Sistemas de control de versiones - 37

class Nodo:
    def __init__(self):
        self.dato = None
        self.siguiente = None

class lista_enlazada:
    def __init__(self):
        self.cabeza = None

    def vacia(self):
        return self.cabeza is None
    
    def agregar_inicio(self, dato):
        nuevo_nodo = Nodo(dato)
        nuevo_nodo.siguiente = self.cabeza
        self.cabeza = nuevo_nodo

    def agregar_final(self, dato):
        nuevo_nodo = Nodo(dato)
        if self.vacia():
            self.cabeza = nuevo_nodo
            return
        
        actual = self.cabeza
        while actual.siguiente:
            actual = actual.siguiente
        actual.siguiente = nuevo_nodo

    def agregar_posicion(self, dato, posicion):
        if posicion == 0:
            self.agregar_inicio(dato)
            return
        
        nuevo_nodo = Nodo(dato)
        actual = self.cabeza
        indice = 0

        while actual and indice < posicion - 1:
            actual = actual.siguiente
            indice += 1

        if actual is None:
            print("Posición fuera de rango")
            return
        
        nuevo_nodo.siguiente = actual.siguiente
        actual.siguiente = nuevo_nodo

        