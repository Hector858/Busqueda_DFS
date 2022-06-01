#Se importa la librería queue de python
from queue import Queue

class Grafo:
    """
    Una clase que representa el algoritmo de búsqueda por amplitud

    ...

    Atributos
    ----------
    numero_de_nodos : int
            indica el número de nodos que va a llevar el grafo
    dirigido : boolean
            Si el grafo se encuentra en dirigido (True) o no dirigido (False)
            
    Métodos
    -------
    __init__(self, numero_de_nodos, dirigido=Treu):
        Constructor de la clase Grafo
        
        Crea el diccionario de la lista de adyacencia seteando cada nodo.
    añadir_arista(self, nodo1, nodo2, peso):
        Método que agrega una arista al grafo.
        
        Si el primer grafo no se encuentra dirigido se pasa al siguiente
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
        
        #Si el grafo no esta dirigido se agrega la arista al otro nodo
        if not self.m_dirigido:
            #Agregar una arista del nodo 2 de la lista de adyacencia
            self.m_lista_adyacencia[nodo2].add((nodo1, peso))  