import pytest
import unittest
import json
import feedparser
from unittest.mock import MagicMock, patch
import os

from app.app import app
from app.resource import Review as ReviewResource
from app.dto import Review as ReviewDto

RSS_PATH = os.path.abspath('assets/rss/default.rss')

class ReviewTest(unittest.TestCase):
	def setUp(self): 
		self.app = app.test_client()

	def test_review_get_method_exists(self):
		self.assertIsNotNone(ReviewResource().get())

	@patch('feedparser.parse', return_value=feedparser.parse(RSS_PATH))
	def test_review_get_returns_all_reviews(self, parser_function):
		expect = []
		x = feedparser.parse(RSS_PATH)
		for i in range(2):
			expect.append(ReviewDto(
				content=str(x.entries[i].description),
				filmTitle=str(x.entries[i].letterboxd_filmtitle),
				filmYear=str(x.entries[i].letterboxd_filmyear),
				memberRating=str(x.entries[i].letterboxd_memberrating),
				link=str(x.entries[i].link)
			).__dict__)
		self.assertListEqual(ReviewResource().get(), expect)

	@patch('feedparser.parse', return_value=feedparser.parse(RSS_PATH))
	def test_review_get_index(self, parser_function):
		index = 1
		x = feedparser.parse(RSS_PATH)
		expect = ReviewDto(
			content=str(x.entries[index].description),
			filmTitle=str(x.entries[index].letterboxd_filmtitle),
			filmYear=str(x.entries[index].letterboxd_filmyear),
			memberRating=str(x.entries[index].letterboxd_memberrating),
			link=str(x.entries[index].link)
		).__dict__
		self.assertDictEqual(ReviewResource().get(index), expect)
	
	@patch('feedparser.parse', return_value=feedparser.parse(RSS_PATH))
	def test_review_get_index_non_review_rss(self, parser_function):
		with pytest.raises(IndexError):
			index = 2
			ReviewResource().get(index)

	@patch('feedparser.parse', return_value=feedparser.parse(RSS_PATH))
	def test_review_get_route(self, parser_function):
		expect = ReviewResource().get()
		response = self.app.get('/review')
		self.assertListEqual(expect, response.json)

	@patch('feedparser.parse', return_value=feedparser.parse(RSS_PATH))
	def test_review_get_route_index(self, parser_function):
		index = 1
		expect = ReviewResource().get(index)
		response = self.app.get(f'/review/{index}')
		self.assertDictEqual(expect, response.json)