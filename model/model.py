import networkx as nx

from database.DAO import DAO


class Model:
    def __init__(self):

        self.grafo = nx.Graph()
        self._idMap = {}
        self._idMapNome = {}

    def creaGrafo(self, calorie):
        self.nodi = DAO.getNodi(calorie)
        self.grafo.add_nodes_from(self.nodi)
        self.addEdges(calorie)
        return self.grafo

    def getNumNodes(self):
        return len(self.grafo.nodes)

    def getNumEdges(self):
        return len(self.grafo.edges)

    def addEdges(self, calorie):
        self.grafo.clear_edges()
        allEdges = DAO.getConnessioni(calorie)
        for connessione in allEdges:
            nodo1 = connessione.v1
            nodo2 = connessione.v2
            if nodo1 in self.grafo.nodes and nodo2 in self.grafo.nodes:
                if self.grafo.has_edge(nodo1, nodo2) == False:
                    self.grafo.add_edge(nodo1, nodo2, weight=connessione.peso)
    def getAnalisi(self,tipo):
        analisi=[]
        for vicini in self.grafo.neighbors(tipo):
            analisi.append((vicini,self.grafo[vicini][tipo]["weight"]))
        return analisi



