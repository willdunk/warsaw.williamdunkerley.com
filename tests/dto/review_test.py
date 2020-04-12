import pytest
import unittest
from app.dto import Review as ReviewDto

class TestReview(unittest.TestCase):
	def test_review_default_none(self):
		expect = {
			'content': None,
			'filmTitle': None,
			'filmYear': None,
			'memberRating': None,
			'link': None,
			'backdrop': None,
		}
		self.assertDictEqual(ReviewDto().__dict__, expect)
	
	def test_review_assigns_attributes(self):
		[content, filmTitle, filmYear, memberRating, link, backdrop] = [
			"contentHere",
			"filmTitleHere",
			"filmYearHere",
			"memberRatingHere",
			"linkHere",
			"backdropHere"
		]
		expect = {
			'content': content,
			'filmTitle': filmTitle,
			'filmYear': filmYear,
			'memberRating': memberRating,
			'link': link,
			"backdrop": backdrop
		}
		r = ReviewDto(
			content=content,
			filmTitle=filmTitle,
			filmYear=filmYear,
			memberRating=memberRating,
			link=link,
			backdrop=backdrop
		).__dict__
		self.assertDictEqual(r, expect)