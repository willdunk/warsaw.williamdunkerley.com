from flask_restful import Resource
import feedparser

class ReviewDao():
	def __init__(self, content=None, imageUrl=None):
		self.content = content
		self.imageUrl = imageUrl

class Review(Resource):
	def get(self):
		x = feedparser.parse('https://letterboxd.com/hahaveryfun/rss/')
		content = x.entries[0].description
		r = ReviewDao(str(content), None)		
		return r.__dict__
