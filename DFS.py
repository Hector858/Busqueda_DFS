#Se importa la librería queue de python
from queue import Queue

class Grafo:
    """
    Una clase que representa el algoritmo de búsqueda por profundidad

    ...

    Atributos
    ----------
    numero_de_nodos : int
            indica el número de nodos que va a llevar el grafo
    dirigido : boolean
            Si el grafo se encuentra en dirigido (True) o no dirigido (False)
    nodo1 : int 
            Nodo 1 o de inicio
    nodo2 : int
            Nodo 2 o de fin
    peso : int 
            Peso de la arista
            
            Este atributo puede tener un valor opcional (proporcionado por uno mismo)
    nodo_inicio : int  
            Nodo inicial del recorrido
    inicial : int 
            Nodo 1 o de inicio
    objetivo : int
            Nodo 2 o de fin
    visitado: list
            Conjunto vacío de nodos visitados
    camino : list
            Lista vacia
    Returns:
            camino : list
                Lista del camino recorrido
            resultado: list
                resultado del par ordenado
            
    Métodos
    -------
    __init__(self, numero_de_nodos, dirigido=Treu):
        Constructor de la clase Grafo
        
        Crea el diccionario de la lista de adyacencia seteando cada nodo.    
    agregar_arista(self, nodo1, nodo2, peso):
        Método que agrega una arista al grafo.
        
        Si el primer grafo no se encuentra dirigido se pasa al siguiente  
    imprimir_lista_adyacencia(self):
        Método que imprime la lista de adyacencia.
        
        Imprime la lista de adyacencia de los nodos por cada una de sus llaves.   
    dfs(self, inicial, objetivo, camino = [], visitado = set()):
        Método que realiza un recorrido del grafo por profundidad
        
        Realiza un proceso recursivo para volver a preguntar si es igual al objetivo 
    Main
    -------- 
    __main__
        Main de la clase Grafo
        
        Imprime los nodos nodos asignados y muestra el camino recorrido
    """
    # Constructor
    def __init__(self, numero_de_nodos, dirigido=True):#self es uno mismo
        '''
        Constructor de la clase Grafo
        
        Crea el diccionario de la lista de adyacencia seteando cada nodo.
        
        
            Parámetros: 
            ----------
            numero_nodos: int   
                    Número de nodos que posee el grafo
            dirigido: boolean 
                    Si el grafo es dirigido (true) o no dirigido (false)
        '''
        self.m_numero_de_nodos = numero_de_nodos#El número de nodos
        self.m_nodos = range(self.m_numero_de_nodos)#genera un rango del número de nodos
		
        #Indica dentro del contructor si es dirigido o no dirigido
        self.m_dirigido = dirigido
		
        # Representación grafo - Lista de adyacencia
        # En python esto es un diccionario e implementar una lista de adyacencia
        self.m_lista_adyacencia = {
            node: set() for node in self.m_nodos#Hace un ciclo de repetición en los nodos para setearlos cada uno
            }
        
    # Función que agrega una arista al grafo
    def agregar_arista(self, nodo1, nodo2, peso=1):
        '''
        Método que agrega una arista al grafo.
        
        Si el primer grafo no se encuentra dirigido se pasa al siguiente
        
        Se definen los nodos y el peso va a hacer un valor opcional (puede ser cualquiera)
        
            Parámetros:
            ----------
            nodo1 : int 
                    Nodo 1 o de inicio
            nodo2 : int
                    Nodo 2 o de fin
            peso : int 
                    Peso de la arista
                    
                    Este atributo puede tener un valor opcional (proporcionado por uno mismo)
        '''
        #Agregar una arista del nodo 1 a la lista de adyacencia
        self.m_lista_adyacencia[nodo1].add((nodo2, peso))
        
        #Si el nodo no esta dirigido se agrega la arista al otro nodo
        if not self.m_dirigido:
            #Agregar una arista del nodo 2 de la lista de adyacencia
            self.m_lista_adyacencia[nodo2].add((nodo1, peso))  
           
    # Función que imprime la representación del grafo
    def imprimir_lista_adyacencia(self):
        ''' 
        Método que imprime la lista de adyacencia por medio de una matriz.
        
        Imprime la lista de adyacencia de los nodos por cada una de sus llaves.
        '''
        #Realiza un recorrido en la lista de adyacencia a través de sus llaves
        for llave in self.m_lista_adyacencia.keys():
            #Imprime cada uno de los nodos que se encuentren en la lista de adyacencia
            #colocan donde se dirigen los nodos y su peso
            print("nodo", llave, ": ", self.m_lista_adyacencia[llave])
    #Función que realiza el recorrido DFS
    def dfs(self, inicial, objetivo, camino = [], visitado = set()):
        '''
        Método que realiza un recorrido del grafo por profundidad
        
        Retorna el par ordenado
        
        Realiza un proceso recursivo para volver a preguntar si es igual al objetivo
        
            Parámetros:
            ----------
            inicial : int 
                    Nodo 1 o de inicio
            objetivo : int
                    Nodo 2 o de fin
            visitado: list
                    Conjunto vacío de nodos visitados
            camino : list
                    Lista vacia
            Returns:
                camino : list
                    Lista del camino recorrido
                resultado: list
                    resultado del par ordenado
                
        '''
        #Agrega el item del nodo inicial a la lista del camino
        camino.append(inicial)
        #Agrega el nodo inicial al lista de visitado
        visitado.add(inicial)
        #Si el inicial es igual al objetivo se acaba la ejecución
        #porque no tiene que recorrer más
        if inicial == objetivo:
            #Se retorna la lista del camino
            return camino
        #recorre el nodo vecino del inicio de lista de adyacencia
        for (vecino, peso) in self.m_lista_adyacencia[inicial]:
            #indica si el nodo vecino no ha sido visitado
            if vecino not in visitado:
                #Se realiza un proceso recursivo para preguntar si es igual al objetivo
                resultado = self.dfs(vecino, objetivo, camino, visitado)
                #Si es resultado no es ninguna
                if resultado is not None:
                    #retorna el par ordenado
                    return resultado
        #Elimina y retorna un elemento de la lista de camino
        camino.pop()
        #indica que no hay valor posible que devolver
        return None
    
if __name__ == "__main__":
    '''
        Main de la clase Grafo.
        
        Imprime los nodos nodos asignados y muestra el camino recorrido
        
    '''
        
    # Crea una instancia de la clase "Grafo"
    # Este grafo es no dirigido y tiene 5 nodos
    g = Grafo(5, dirigido=False)
    
    # Agrega las aristas del grafo
    g.agregar_arista(0,1)# Agrega la arista (0,1) con peso=1
    g.agregar_arista(0,2)# Agrega la arista (0,2) con peso=1
    g.agregar_arista(1,2)# Agrega la arista (1,2) con peso=1
    g.agregar_arista(1,4)# Agrega la arista (1,4) con peso=1
    g.agregar_arista(2,3)# Agrega la arista (2,3) con peso=1
    
    # Imprime la lista de adyacencia en el formulario del nodo
    g.imprimir_lista_adyacencia()
    
    #lista vacía del camino del recorrido
    camino_recorrido = []
    #Se intancia el camino del recorrido
    #desde el nodo 0 al nodo 3
    camino_recorrido = Grafo.dfs(0, 3)
    #Imprime el camino del recorrido
    print(f" El camino del recorrido del nodo 0 al nodo 3 es {camino_recorrido}")