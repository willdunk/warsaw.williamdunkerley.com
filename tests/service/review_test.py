import pytest
import unittest
import feedparser
from unittest.mock import MagicMock, Mock, patch
import os

from app.app import app
from app.service import Review as ReviewService
from app.dto import Review as ReviewDto

RSS_PATH = os.path.abspath('assets/rss/default.rss')

class TestReview(unittest.TestCase):
	def setUp(self): 
		self.app = app.test_client()

	def test_review_get_reviews_exists(self):
		self.assertIsNotNone(ReviewService().getReviews)

	@patch('feedparser.parse', return_value=feedparser.parse(RSS_PATH))
	def test_review_get_reviews_parses(self, parser_function):
		expect = []
		x = feedparser.parse(RSS_PATH)
		for i in range(2):
			expect.append(ReviewDto(
				content=str(x.entries[i].description),
				filmTitle=str(x.entries[i].letterboxd_filmtitle),
				filmYear=str(x.entries[i].letterboxd_filmyear),
				memberRating=str(x.entries[i].letterboxd_memberrating),
				link=str(x.entries[i].link)
			))
		self.assertListEqual(ReviewService().getReviews(), expect)

	def test_review_get_review_exists(self):
		self.assertIsNotNone(ReviewService().getReview)

	@patch('app.service.Review.getReviews', return_value=[ReviewDto("content1"), ReviewDto("content2")])
	def test_review_get_review(self, get_reviews_mock):
		self.assertEqual(ReviewService().getReview(0), ReviewDto("content1"))