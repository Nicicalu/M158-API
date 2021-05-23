#from app.main.Config import Config
from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps
from pyowm.utils.config import get_default_config
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
        