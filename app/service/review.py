from app.app import db
from typing import List
from app.model import ReviewModel

class Review():
	def getReviews(self) -> List[ReviewModel]:
		return ReviewModel.query.order_by(ReviewModel.title).all()

	def getReview(self, index) -> ReviewModel:
		return ReviewModel.query.filter_by(review_id=index).first()