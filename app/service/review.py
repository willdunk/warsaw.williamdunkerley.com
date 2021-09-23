from app.app import db
from typing import List
from app.model import ReviewModel

class Review():
	def getReviews(self, page_number=None, page_size=None, order_by='published_date', order_direction='DESC') -> List[ReviewModel]:
		column = {
			'title': ReviewModel.title,
			'published_date': ReviewModel.published_date,
			'watched_date': ReviewModel.watched_date
		}[order_by]
		column_ordered = {
			'ASC': column.asc(),
			'DESC': column.desc()
		}[order_direction]
		query = ReviewModel.query.order_by(column_ordered)
		if page_number is None and page_size is None:
			return query.all()
		return query.paginate(page_number, page_size, True).items

	def getReview(self, index) -> ReviewModel:
		return ReviewModel.query.filter_by(review_id=index).first()
