from app.main.controller.__init__ import cursor

# Funktion für das Ausführen von Datenbank Queries
def databaseQuery(query):
    cursor.execute(query) # Query ausführen
    result = cursor.fetchall() # Ganzes Resultat auslesen
    return result