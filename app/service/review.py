from app.app import db
from typing import List
from app.model import ReviewModel

class Review():
	def getReviews(self, page_number=None, page_size=None, order_by='published_date', order_direction='DESC') -> List[ReviewModel]:
		print(page_number)
		print(page_size)
		print(order_by)
		print(order_direction)
		column = {
			'title': ReviewModel.title,
			'published_date': ReviewModel.published_date,
			'watched_date': ReviewModel.watched_date
		}[order_by]
		column_ordered = {
			'ASC': column.asc(),
			'DESC': column.desc()
		}[order_direction]
		return ReviewModel.query.order_by(column_ordered).paginate(page_number, page_size, True).items

	def getReview(self, index) -> ReviewModel:
		return ReviewModel.query.filter_by(review_id=index).first()
