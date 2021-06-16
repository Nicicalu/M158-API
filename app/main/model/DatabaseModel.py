from app.main.controller.__init__ import cursor, cnxn

# Funktion für das Ausführen von Datenbank Queries
def databaseQuery(query):
    print("Execute Query "+query)
    cursor.execute(query) # Query ausführen
    if "SELECT" in query: #Wenn SELECT Query
        result = cursor.fetchall() # Ganzes Resultat auslesen
        data = [] #Daten kommen hier rein
        columns = [column[0] for column in cursor.description] #Alle Spalten in eine Variable
        for record in result:
            data.append( dict( zip( columns , record ) ) ) #Alle Daten zusammen mit Spalten Überschriften in eine List packen
    else:
        cnxn.commit() #Transaction ausführen
        data = "Success" #Success :)
    return data
    