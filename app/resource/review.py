from flask_restx import Resource, Namespace, reqparse
from app.service import Review as ReviewService
from app.app import api
from app.utils import review_fields

api = Namespace('review', description='Review operations')

parser = reqparse.RequestParser()
parser.add_argument('page_number', location="args", type=int)
parser.add_argument('page_size', location="args", type=int)
parser.add_argument('order_by', location="args", choices=('title', 'published_date', 'watched_date'), default='published_date')
parser.add_argument('order_direction', location="args", choices=('ASC', 'DESC'), default='ASC')

@api.route('')
class Reviews(Resource):
	@api.doc(security=None)
	@api.expect(parser)
	@api.marshal_with(review_fields)
	def get(self):
		return ReviewService().getReviews(**parser.parse_args())

@api.route('/<string:review_uuid>')
class Review(Resource):
	@api.doc(security=None)
	@api.marshal_with(review_fields)
	def get(self, review_uuid):
		return ReviewService().getReview(review_uuid)
