from flask_restx import Resource, Namespace
from app.service import Review as ReviewService
from app.app import api
from app.utils import review_fields

api = Namespace('review', description='Review operations')

@api.route('')
class Reviews(Resource):
	@api.doc(security=None)
	@api.marshal_with(review_fields)
	def get(self):
		return ReviewService().getReviews()

@api.route('/<string:review_uuid>')
class Review(Resource):
	@api.doc(security=None)
	@api.marshal_with(review_fields)
	def get(self, review_uuid):
		return ReviewService().getReview(review_uuid)
