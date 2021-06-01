from app.main.model.DatabaseModel import databaseQuery
import hashlib

def login(username, password):

    # Zu SHA256 Hash verschlüsseln
    sha_password = hashlib.sha256(password.encode()).hexdigest()
    print("Hash: "+sha_password)
    # Passwort-Hash mit Datenbank vergleichen, gibt es einen User mit diesem Benutzernamen und Passwort-Hash?
    result = databaseQuery("Select * FROM tbl_login WHERE `username` = '"+username+"' AND `password` = '"+sha_password+"'")

    return result