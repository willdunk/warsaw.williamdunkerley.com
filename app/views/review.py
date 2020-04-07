from flask_restful import Resource

class ReviewDao():
	def __init__(self, text):
		self.text = text

class Review(Resource):
	def get(self):
		r = ReviewDao("text")
		return r.__dict__
