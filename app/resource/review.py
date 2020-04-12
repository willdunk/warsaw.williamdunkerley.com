from flask_restful import Resource
import feedparser
from app.service import Review as ReviewService
from app.dto import Review as ReviewDto
from app.app import api

@api.resource('/review', '/review/<int:index>')
class Review(Resource):
	def __init__(self):
		self.service = ReviewService()
	def get(self, index=None):
		if index is None:
			return list(map(lambda review: review.__dict__, self.service.getReviews()))
		else:
			return self.service.getReview(index).__dict__
