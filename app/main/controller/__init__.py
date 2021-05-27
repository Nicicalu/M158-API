#from app.main.Config import Config
import pyodbc


try:
    cnxn = pyodbc.connect("Driver={ODBC Driver 17 for SQL Server};"
                        "Server=WS2;"
                        "Database=Noten;"
                        "uid=Api;pwd=sml12345")
    cursor = cnxn.cursor()
    print("Connected to SQL Server successfully")

except:
    print("Error while connecting to MSSQL")
        