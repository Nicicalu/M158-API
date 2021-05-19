import re
from flask import request, jsonify
from flask_cors import CORS, logging, cross_origin
from flask_restplus import Resource, Namespace, reqparse
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


# Route für Login
@api.route('/login')
@api.doc('Route for logging in')
@api.response(200, 'Login auth as json')
class handleQuestion(Resource):
    
    def post(self):
        username = request.json["username"]
        password = request.json["password"]
        databaseQuery("Select * FROM tbl_login WHERE `username` = '"+username+"' AND `password` = '"+password+"'")

        print("----- Login ------")
        print("Benutzername: "+username)
        print("Passwort: "+password)
        return "Login successful"

# Daten aus Datenbank holen
@api.route('/anrede')
@api.doc('Route for getting data of "anrede"')
@api.response(200, 'selected data')
class handleQuestion(Resource):
    
    def post(self):
        table = request.json["table"]

        data = databaseQuery("Select * FROM "+table)

        return str(data)
