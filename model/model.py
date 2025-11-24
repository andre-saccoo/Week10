from database.DAO import DAO
import networkx as nx

class Model:
    def __init__(self):
        self._lista_fermate= []
        self._dizionario_fermate = {}
        self._grafo = None
        pass
    def getAllFermate(self):
        fermate=DAO.readAllFermate()
        self._lista_fermate=fermate
        for fermata in self._lista_fermate:
            self._dizionario_fermate[fermata._id_fermata]=fermata

    def creaGrafo(self):
        self._grafo=nx.Graph() #grafo vuoto
        for fermata in self._lista_fermate:
            self._grafo.add_node(fermata)
        #primo modo di aggiungere i nodi con 619x 619 query ->lento
        """for u in self._grafo: #per ognuno dei 619 nodi
            for v in self._grafo[u]: #per ognuno dei possibili nodi controllo se è connesso con gli altri nodi
                risultato=DAO.existsConnessioneTra(u,v)
                if(len(risultato)>0):
                    self._grafo_edge(u,v)
                    print(f"Aggiunto arco tra {u} e {v}")
        """
        for u in self._grafo:
            connessioni = DAO.searchViciniFermata(u)
            for connessione in connessioneVicini:
                fermataArrivo=self._dizionario_fermate[connessione._id_fermata]
                self._grafo.add_edge(u,fermataArrivo)