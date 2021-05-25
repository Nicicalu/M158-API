
def generate_insert_query(dictionary, table):
    
    # Get all "keys" inside dictionary (column names)
    columns = ', '.join(dictionary.keys())  

    # Get all "values" inside of dictionary (insert values)
    values = ', '.join(dictionary.values())

    # Generate INSERT query
    print(f"INSERT INTO {table} ({columns}) VALUES ({values})" + "\n")

def generate_update_query(dictionary, table):

    # Get all "keys" inside dictionary (column names)
    columns = ', '.join(dictionary.keys())  

    # Get all "values" inside of dictionary (insert values)
    values = ', '.join(dictionary.values())

    # Generate INSERT query
    print(f"INSERT INTO {table} ({columns}) VALUES ({values})" + "\n")