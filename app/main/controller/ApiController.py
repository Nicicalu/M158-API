import re
from flask import request, jsonify
from flask_cors import CORS, logging, cross_origin
from flask_restplus import Resource, Namespace, reqparse

api = Namespace('api', description='api operations')

# if method == 'POST':

@api.route('/')
@api.doc('TEST OPERATION')
@api.response(200, 'Test was successful')
class DoUser(Resource):
    @cross_origin()
    def post(self):
        return "Test successful"


@api.route('/login')
@api.doc('Route for logging in')
@api.response(200, 'Login auth as json')
class handleQuestion(Resource):
    
    def post(self):
        username = request.json["username"]
        password = request.json["password"]
        return "Hello World!"
