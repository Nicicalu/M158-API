from app.main.model.DatabaseModel import databaseQuery
from app.main.service.HelperService import generate_insert_query, generate_update_query

# Funktion für das Hinzufügen von Daten
def insert(data, table):
    query = generate_insert_query(data, table) # Query generieren lassen
    result = databaseQuery(query) #Query ausführen
    return result

# Funktion für das Hinzufügen von Daten
def add(data, table):
    query = generate_insert_query(data, table) # Query generieren lassen
    result = databaseQuery(query) #Query ausführen
    return result

# Funktion für das Ändern von Daten
def update(data, table):
    query = generate_update_query(data, table) # Query generieren lassen
    result = databaseQuery(query) #Query ausführen
    return result