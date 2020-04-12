from flask_restful import Resource
import feedparser
from app.dto import Review as ReviewDto
from app.app import api
from typing import List

class Review():
	def getReviews(self) -> List[ReviewDto]:
		feed = feedparser.parse('https://letterboxd.com/hahaveryfun/rss/')
		entries = list(filter(lambda entry: 'letterboxd-review' in entry.id, feed.entries))
		def makeDto(entry):
			return ReviewDto(
				content=str(entry.description),
				filmTitle=str(entry.letterboxd_filmtitle),
				filmYear=str(entry.letterboxd_filmyear),
				memberRating=str(entry.letterboxd_memberrating),
				link=str(entry.link)
			)
		return list(map(makeDto, entries))

	def getReview(self, index) -> ReviewDto:
		lst = self.getReviews()
		return lst[index]