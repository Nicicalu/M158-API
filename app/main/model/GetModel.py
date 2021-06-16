from app.main.model.DatabaseModel import databaseQuery

# Funktion für das auslesen von Daten
def get(table):
    sqlQuery = "SELECT * FROM tbl_" + table + "" #SELECT Query erstellen
    try:
        data = databaseQuery(sqlQuery) #Query ausführen
    except:
        print("--------- FEHLER BEI GET QUERY ---------") #Fehler in terminal ausgeben
        data = "Fehler. Query '"+sqlQuery+"' konnte nicht ausgeführt werden." #Fehler zurückgeben
    return data