from app.main.controller.__init__ import cursor

def databaseQuery(query):
    cursor.execute(query)
    result = cursor.fetchall()
    return result;