from database.DB_connect import DBConnect
from model.Connessione import Connessione
from model.Fermata import Fermata

class DAO():
    @staticmethod
    def readAllFermate(): #quando mi serve lo chiamo senza passargli l'oggetto stesso
        conn= DBConnect.get_connection()
        result=[]
        query="SELECT * FROM Fermata"
        cursor = conn.cursor(dictionary= True)
        cursor.execute(query)
        for row in cursor:
            fermata=Fermata(row["id_fermata"],row["nome"])
            result.append(fermata)
        cursor.close()
        conn.close()
        return result

    def existConnessioneTra(u:Fermata):
        conn = DBConnect.get_connection()
        # Verifica se esista una connessione tra gli id dati e te le elenca
        result = []
        query = """SELECT * FROM connessione c WHERE c.id_stazP =%S """# prendo tutte le connessioni che hanno la stazione di partenza passata come parametro
        cursor = conn.cursor(dictionary=True)
        cursor.execute(query,(u.id_fermata , ))
        for row in cursor:
            connessione = Connessione(row["id_connessione"],row["id_linea"],row["id_stazP",row["id_stazP"]]) #creo oggetto di tipo connessione e lo salvo
            result.append(connessione)
            print(row)
        cursor.close()
        conn.close()
        return result

    @staticmethod
    def searchViciniAFermata(u: Fermata):
        # Cerco le fermate collegate a quella passata come parametro
        cnx = DBConnect.get_connection()
        result = []
        query = """select *
                        from connessione c
                        where c.id_stazP = %s """

        cursor = cnx.cursor(dictionary=True)
        cursor.execute(query, (u.id_fermata,))

        for row in cursor:
            connessione = Connessione(row["id_connessione"],
                                      row["id_linea"],
                                      row["id_stazP"],
                                      row["id_stazA"])
            result.append(connessione)

        cursor.close()
        cnx.close()
        return result