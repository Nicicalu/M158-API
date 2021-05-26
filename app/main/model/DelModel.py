from app.main.model.DatabaseModel import databaseQuery

# Funktion für das Löschen von Daten
def delete(data, table):
    column = list(data.keys())[0] # erste Spalte
    value = list(data.values())[0] # erster Wert
    sqlQuery = "DELETE FROM tbl_" + table + " WHERE "+str(column)+" = '"+str(value)+"'" #Delete Query zusammenbauen
    try:
        data = databaseQuery(sqlQuery) #Query ausführen
    except:
        print("--------- FEHLER BEI DELETE QUERY ---------")
        data = "Fehler. Query '"+sqlQuery+"' konnte nicht ausgeführt werden."
    return data