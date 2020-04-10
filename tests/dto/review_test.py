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
		}
		self.assertDictEqual(ReviewDto().__dict__, expect)
	
	def test_review_assigns_attributes(self):
		[content, filmTitle, filmYear, memberRating, link] = [
			"contentHere",
			"filmTitleHere",
			"filmYearHere",
			"memberRatingHere",
			"linkHere"
		]
		expect = {
			'content': content,
			'filmTitle': filmTitle,
			'filmYear': filmYear,
			'memberRating': memberRating,
			'link': link,
		}
		r = ReviewDto(
			content=content,
			filmTitle=filmTitle,
			filmYear=filmYear,
			memberRating=memberRating,
			link=link
		).__dict__
		self.assertDictEqual(r, expect)