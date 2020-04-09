from flask_restful import Resource
import feedparser
from app.dto import Review as ReviewDto
from app.app import api

@api.resource('/review', '/review/<int:index>')
class Review(Resource):
	def get(self, index=None):
		feed = feedparser.parse('https://letterboxd.com/hahaveryfun/rss/')
		entries = list(filter(lambda entry: 'letterboxd-review' in entry.id, feed.entries))
		def makeDto(entry):
			return ReviewDto(
				content=str(entry.description),
				filmTitle=str(entry.letterboxd_filmtitle),
				filmYear=str(entry.letterboxd_filmyear),
				memberRating=str(entry.letterboxd_memberrating),
				link=str(entry.link)
			).__dict__
		if index is None:
			return list(map(makeDto, entries))
		else:
			return makeDto(entries[index])
