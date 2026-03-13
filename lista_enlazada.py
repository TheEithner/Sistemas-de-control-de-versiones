# Eithner Geovanny Palacios Palacios
# Sistemas de control de versiones - 37

class Nodo:
    def __init__(self):
        self.dato = None
        self.siguiente = None

    def __str__(self):
        return str(self.dato)

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

    def eliminar_valor(self, valor):
        if self.vacia():
            return
        
        if self.cabeza.dato == valor:
            self.cabeza = self.cabeza.siguiente
            return
        
        actual = self.cabeza
        while actual.siguiente and actual.siguiente.dato != valor:
            actual = actual.siguiente

        if actual.siguiente:
            actual.siguiente = actual.siguiente.siguiente
        else:
            print(f"Valor {valor} no encontrado en la lista")

    def buscar(self, valor):
        actual = self.cabeza 
        posicion = 0
        while actual:
            if actual.dato == valor:
                print(f"Valor {valor} encontrado en la poicion {posicion}")
                return
            
            actual = actual.siguiente
            posicion += 1
        print(f"Valor {valor} no encontrado en la lista")
        return
    
    def mostrar(self):
        actual = self.cabeza
        elementos = []
        while actual:
            elementos.append(str(actual.dato))
            actual = actual.siguiente
        print(" -> ".join(elementos) + " -> NULL")

    def contar_nodos(self):
        contador = 0
        actual = self.cabeza
        while actual:
            contador += 1
            actual = actual.siguiente
        return contador
    
    def mostrar_ordenada(self):
        datos = []
        actual = self.cabeza
        while actual:
            datos.append(actual.dato)
            actual = actual.siguiente
        datos.sort()

        elementos_ordenados = [str(d) for d in datos]
        print(" -> ".join(elementos_ordenados) + " -> NULL")

