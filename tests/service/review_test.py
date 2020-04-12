import pytest
import unittest
import feedparser
from unittest.mock import MagicMock, Mock, patch, PropertyMock
import os
import requests_mock

from app.app import app
from app.service import Review as ReviewService
from app.dto import Review as ReviewDto

RSS_PATH = os.path.abspath('assets/rss/default.rss')

class TestReview(unittest.TestCase):
	def setUp(self): 
		self.app = app.test_client()

	def test_review_get_reviews_exists(self):
		self.assertIsNotNone(ReviewService().getReviews)

	@patch('app.service.Review.parseLetterboxdPage', return_value="backdropLink")
	@patch('feedparser.parse', return_value=feedparser.parse(RSS_PATH))
	def test_review_get_reviews_parses(self, parseLetterboxdPage_mock, parser_function):
		expect = []
		x = feedparser.parse(RSS_PATH)
		for i in range(2):
			expect.append(ReviewDto(
				content=str(x.entries[i].description),
				filmTitle=str(x.entries[i].letterboxd_filmtitle),
				filmYear=str(x.entries[i].letterboxd_filmyear),
				memberRating=str(x.entries[i].letterboxd_memberrating),
				link=str(x.entries[i].link),
				backdrop="backdropLink"
			))
		self.assertListEqual(ReviewService().getReviews(), expect)
	
	def test_parse_letterboxd_page(self):
		expected = "expectedText"
		demo = f"<body><div><div data-backdrop2x=\"{expected}\"></div></div></body>"
		with requests_mock.Mocker() as mock_request:
			url = "http://asdf.com/asdf"
			mock_request.get(url, text=demo)
			self.assertEqual(expected, ReviewService().parseLetterboxdPage("http://asdf.com/hahaveryfun/asdf"))

	def test_review_get_review_exists(self):
		self.assertIsNotNone(ReviewService().getReview)

	@patch('app.service.Review.parseLetterboxdPage', return_value="backdropLink")
	@patch('app.service.Review.getReviews', return_value=[ReviewDto("content1"), ReviewDto("content2")])
	def test_review_get_review(self, parseLetterboxdPage_mock, get_reviews_mock):
		self.assertEqual(ReviewService().getReview(0), ReviewDto("content1"))