from app.main.model.DatabaseModel import databaseQuery
from app.main.service.HelperService import generate_insert_query, generate_update_query

def add(data, table):
    query = generate_insert_query(data, table)
    result = databaseQuery(query)
    return result

def update(data, table):
    query = generate_update_query(data, table)
    result = databaseQuery(query)
    return result