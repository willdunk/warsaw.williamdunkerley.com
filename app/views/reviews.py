from flask_restful import Resource
from .review import ReviewDao

class Reviews(Resource):
	def get(self):
		a = ReviewDao("a")
		b = ReviewDao("b")
		c = ReviewDao("c")
		lst = [a.__dict__, b.__dict__, c.__dict__]
		return lst
