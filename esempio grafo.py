import networkx as nx
import flet as ft
from dataclasses import dataclass
@dataclass
class Amico:
    id: str
    nome: str
    def __str__(self):
        return f"{self.id} {self.nome}"
    #per poter utilizzare l'oggetto come nodo di un grafo
    def __hash__(self):
        return hash(self.id)


g = nx.Graph() #grafo indiretto
g.add_node(1) # funzione che aggiunge un nodo al grafo es nodo 1
g.add_node(2)
# g.add_node('abcd') il nodo può essere qualsiasi cosa anche stringhe, oggetti, etichette flet ft.text...
#a= Amico(2345, "Mario")
#g.add_node(a)
#g.add_edge(1, 2, attributo = "pippo")
g.add_edge(1, 2)
g.add_edge(2, 3) #se non l'hai ancora definito lo definisce lui
g.add_edge(2, 3) #aggiunegere due volte un edge su un grafo normale non c'è problema con il multigraph è differente
#gli archi sono dizionari
print(f"stampo arco{g[1][2]}")

altri_nodi = [4 ,5 ,6 ,7, 8]
g.add_nodes_from(altri_nodi)
altri_archi = [(2,4),(4,5),(6,7),(6,8), (1,4)]
g.add_edges_from(altri_archi)
print (g)
print (g.nodes) #sono riportati nell'ordine di inserimento
print (g.edges)
primo_nodo=g[1]
print(primo_nodo) #ci dice che il nodo uno è collegato a 2 e 4

densità=nx.density(g)
print (densità)


if 12 in g :
    print("nodo presente")
else:
    print("non presente nodo")
for nodo in g:
    print(nodo)
for nodo in g[1]: #stampo i vicini del nodo
    print(nodo)

dg=nx.DiGraph()
dg.add_nodes_from(altri_nodi)
dg.add_edges_from(altri_archi)
print(dg.edges)
print(dg[4]) #mi dice che c'è un arco verso 5
print(dg[5]) #mi dice che non ci sono archi verso 5

mg=nx.MultiGraph()
mg.add_edge(1,2)
mg.add_edge(1,2)
mg.add_edge(1,2)
print(mg[1])
print(f"arco tra 1 e 2 0_esimo: {mg[1][2][0]}")
