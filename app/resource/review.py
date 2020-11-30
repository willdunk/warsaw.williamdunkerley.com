from flask_restx import Resource, Namespace
from app.service import Review as ReviewService
from app.app import api
from flask_jwt_extended import jwt_required, jwt_optional, get_jwt_identity
from app.utils import review_fields

api = Namespace('review', description='Review operations')

@api.route('')
class Reviews(Resource):
	@api.marshal_with(review_fields)
	def get(self):
		return ReviewService().getReviews()

@api.route('/<string:review_uuid>')
class Review(Resource):
	@api.marshal_with(review_fields)
	def get(self, review_uuid):
		return ReviewService().getReview(review_uuid)
