from flask import Flask
from flask_cors import CORS
from flask_restful import Api
from app.views.review import Review
from app.views.reviews import Reviews

app = Flask(__name__)
CORS(app)
api = Api(app)

api.add_resource(Review, '/review')
api.add_resource(Reviews, '/reviews')
