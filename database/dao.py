from database.DB_connect import DBConnect
from database.rifugioDTO import Rifugio
from database.connessioneDTO import Connessione

class DAO:
    """
    Implementare tutte le funzioni necessarie a interrogare il database.
    """
    # TODO
    pass

    @staticmethod
    def crea_nodes(year):
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)

        query = """ select * from rifugio
                    where id in (select id_rifugio1 from connessione where anno <= %s)
                    or id in (select id_rifugio2 from connessione where anno <= %s)"""
        cursor.execute(query,(year,year,))
        lista_nodi=[]

        for row in cursor:
            lista_nodi.append(Rifugio(row["id"], row["nome"], row["localita"],
                                      row["altitudine"],row["capienza"],row["aperto"]))

        cnx.close()
        cursor.close()
        return lista_nodi

    @staticmethod
    def crea_edges(year):
        cnx = DBConnect.get_connection()

        cursor = cnx.cursor(dictionary=True)

        query= """ select * from connessione where anno <= %s """
        cursor.execute(query,(year,))
        lista_edges=[]
        for row in cursor:
            lista_edges.append(Connessione(row["id"], row["id_rifugio1"], row["id_rifugio2"],
                                       row["distanza"], row["difficolta"], row["durata"], row["anno"]))

        cnx.close()
        cursor.close()
        return lista_edges











