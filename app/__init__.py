# app/__init__.py

from flask_restplus import Api
from flask import Blueprint

from .main.controller.ApiController import api as API

blueprint = Blueprint('api', __name__)

api = Api(blueprint,
          title='FLASK RESTPLUS API FOR UNO',
          version='1.0',
          description='a boilerplate for flask restplus web service'
          )

api.add_namespace(API, path='/API')
