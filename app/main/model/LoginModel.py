from app.main.model.DatabaseModel import databaseQuery
import hashlib

def login(username, password):

    # Zu SHA256 Hash verschlüsseln
    sha_password = hashlib.sha256(password.encode()).hexdigest()
    print("Hash: "+sha_password)
    # Passwort-Hash mit Datenbank vergleichen, gibt es einen User mit diesem Benutzernamen und Passwort-Hash?
    result = databaseQuery("SELECT * FROM tbl_Benutzer WHERE benutzername = '"+username+"' AND passwort = '"+sha_password+"'")

    if(len(result) > 0):
        if(result[0]["admin"] == 1):
            return 2
        return 1
    else:
        return 0