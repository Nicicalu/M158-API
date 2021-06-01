import re
import json
from flask import request, jsonify
from flask_cors import CORS, logging, cross_origin
from flask_restplus import Resource, Namespace, reqparse
from app.main.model.GetModel import get
from app.main.model.SetModel import add, update
from app.main.model.DelModel import delete
from app.main.model.LoginModel import login
from app.main.model.DatabaseModel import databaseQuery

api = Namespace('api', description='api operations')


# Standard route /API/ --> gibt zurück, dass die API funktioniert
@api.route('/')
@api.doc('TEST OPERATION')
@api.response(200, 'Test was successful')
class DoUser(Resource):
    @cross_origin()
    def post(self):
        return "Test successful"

@api.route('/get')
@api.doc('Route für das Auslesen von Daten')
@api.response(200, 'Daten als JSON')
class handleQuestion(Resource):
    
    def post(self):
        table = request.json["table"]
        result = get(table)

        return jsonify(result)

@api.route('/set')
@api.doc('Route für das Aktualisieren/Hinzufügen von Daten')
@api.response(200, 'Die Meldung "Success", wenn es funktioniert hat')
class handleQuestion(Resource):
    
    def post(self):
        table = request.json["table"]
        data = request.json["data"]
        action = request.json["action"]

        if(action == "add"):
            result = add(data, table)
        elif (action == "update"):
            result = update(data, table)
        else:
            print("Fehler! Action nicht bekannt")
            return "Fehler! Action nicht bekannt"
        

        return result

@api.route('/del')
@api.doc('Route für das Löschen von Daten')
@api.response(200, 'Die Meldung "Success", wenn es funktioniert hat')
class handleQuestion(Resource):
    
    def post(self):
        table = request.json["table"]
        data = request.json["data"]
        result = delete(data,table)

        return result


# Route für Login
@api.route('/login')
@api.doc('Route for logging in')
@api.response(200, 'Login auth as json')
class handleQuestion(Resource):
    
    def post(self):
        username = request.json["username"]
        password = request.json["password"]
        
        print("----- Login ------")
        print("Benutzername: "+username)
        print("Passwort: "+password)
        
        result = login(username, password)


        return "Login successful"
