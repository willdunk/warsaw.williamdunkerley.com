from flask import Flask
from flask_cors import CORS
from flask_restful import Resource, Api
from app.views.letterboxd import Letterboxd

app = Flask(__name__)
CORS(app)
api = Api(app)

api.add_resource(Letterboxd, '/letterboxd')
