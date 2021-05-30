
def generate_insert_query(dictionary, table):
    
    # Alle "Keys" innerhalb des Dictionarys zusammentragen (Spalten Namen)
    columns = ', '.join(dictionary.keys())  

    # Alle "Values" innerhalb des Dictionarys zusammentragen (Werte einfügen)
    values = ', '.join(dictionary.values())

    # INSERT Query zurückgeben
    return (f"INSERT INTO tbl_{table} ({columns}) VALUES ({values})" + "\n")

def generate_update_query(dictionary, table):

    # Alle "Keys" innerhalb des Dictionarys zusammentragen (Spalten Namen)
    columns = ', '.join(dictionary.keys())  

    # Alle "Values" innerhalb des Dictionarys zusammentragen (Werte einfügen)
    values = ', '.join(dictionary.values())

    # INSERT Query zurückgeben
    return (f"INSERT INTO tbl_{table} ({columns}) VALUES ({values})" + "\n")