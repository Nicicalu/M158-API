from flask import Flask

from .Config import ProductionConfig

from .Config import configByName


def create_app(configName):
    app = Flask(__name__)
    app.config.from_object(configByName[configName])

    return app
