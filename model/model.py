import networkx as nx
from database.dao import DAO

class Model:
    def __init__(self):
        """Definire le strutture dati utili"""
        # TODO
        self.G = nx.Graph()

    def build_weighted_graph(self, year: int):
        """
        Costruisce il grafo pesato dei rifugi considerando solo le connessioni con campo `anno` <= year passato
        come argomento.
        Il peso del grafo è dato dal prodotto "distanza * fattore_difficolta"
        """
        # TODO
        nodi=DAO.crea_nodes(year)

        for el in nodi:
            self.G.add_node(el.id)


        lista_edges = DAO.crea_edges(year)
        for edge in lista_edges:
            if edge.difficolta== "facile":
                peso =  (edge.distanza * 1)
                self.G.add_weighted_edges_from([(edge.id_rifugio1, edge.id_rifugio2, peso)])

            elif edge.difficolta== "media":
                peso = (float(edge.distanza) * 1.5)
                self.G.add_weighted_edges_from([(edge.id_rifugio1, edge.id_rifugio2, peso)])

            elif edge.difficolta== "difficile":
                peso = (edge.distanza * 2)
                self.G.add_weighted_edges_from([(edge.id_rifugio1, edge.id_rifugio2, peso)])

        return self.G


    def get_edges_weight_min_max(self):
        """
        Restituisce min e max peso degli archi nel grafo
        :return: il peso minimo degli archi nel grafo
        :return: il peso massimo degli archi nel grafo
        """
        # TODO

        peso= nx.get_edge_attributes(self.G, 'weight').values()
        return min(peso), max(peso)



    def count_edges_by_threshold(self, soglia):
        """
        Conta il numero di archi con peso < soglia e > soglia
        :param soglia: soglia da considerare nel conteggio degli archi
        :return minori: archi con peso < soglia
        :return maggiori: archi con peso > soglia
        """
        # TODO
        minori=[]
        maggiori=[]

        for u,v, peso in self.G.edges(data=True):

            weight = peso['weight']

            if  weight< soglia :
                minori.append((u,v))

            if  weight > soglia:
                maggiori.append((u,v))

        return len(minori), len(maggiori)




    """Implementare la parte di ricerca del cammino minimo"""
    # TODO
    def cammino_minimo(self, S):

        grafo_minimo= nx.Graph()
        for u,v, peso in self.G.edges(data=True):
            weight = float(peso['weight'])

            if weight > S:
                grafo_minimo.add_weighted_edges_from([(u, v, weight)])

        cammino_minimo=None
        peso_minimo= float('inf')

        for inizio in grafo_minimo.nodes():
            for fine in grafo_minimo.nodes():


                try:
                    dj= nx.dijkstra_path(grafo_minimo, inizio, fine, weight='weight')
                    if len(dj) >= 3:
                        peso = 0
                        organizzato=[]
                        for i in range(len(dj) - 1):
                            u = dj[i]
                            v = dj[i + 1]
                            peso += grafo_minimo[u][v]['weight']
                            organizzato.append(
                                f"[{u}] --> [{v}], peso: {peso}")

                        if peso < peso_minimo:
                            peso_minimo = peso
                            cammino_minimo = organizzato

                except nx.NetworkXNoPath:
                    continue

        return cammino_minimo












