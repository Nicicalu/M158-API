from app.main.model.DatabaseModel import databaseQuery

def get(table):
    sqlQuery = "SELECT * FROM " + table + ""
    data = databaseQuery(sqlQuery);
    return data