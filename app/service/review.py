from flask_restful import Resource
import feedparser
from app.dto import Review as ReviewDto
from app.app import api
from typing import List
from bs4 import BeautifulSoup
import requests

class Review():
	def getReviews(self) -> List[ReviewDto]:
		feed = feedparser.parse('https://letterboxd.com/hahaveryfun/rss/')
		entries = list(filter(lambda entry: 'letterboxd-review' in entry.id, feed.entries))
		def makeDto(entry):
			backdrop = self.parseLetterboxdPage(entry.link)
			return ReviewDto(
				content=str(entry.description),
				filmTitle=str(entry.letterboxd_filmtitle),
				filmYear=str(entry.letterboxd_filmyear),
				memberRating=str(entry.letterboxd_memberrating),
				link=str(entry.link),
				backdrop=str(backdrop)
			)
		return list(map(makeDto, entries))

	def getReview(self, index) -> ReviewDto:
		lst = self.getReviews()
		return lst[index]

	def parseLetterboxdPage(self, review_link):
		text = requests.get(review_link.replace("/hahaveryfun", "")).text
		soup = BeautifulSoup(text, 'html.parser')
		return soup.body.div.div['data-backdrop2x']