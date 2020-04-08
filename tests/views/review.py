import pytest
import unittest
import json
import feedparser
from unittest.mock import MagicMock, patch
import os

from app import app
from app.views.review import Review, ReviewDao

RSS_PATH = os.path.abspath('assets/rss/default.rss')

class ReviewTest(unittest.TestCase):
	def setUp(self): 
		self.app = app.test_client()

	@patch('feedparser.parse', return_value=feedparser.parse(RSS_PATH))
	def test_review_get_class(self, parser_function):
		r = ReviewDao(
			content = feedparser.parse(RSS_PATH).entries[0].description
		)
		self.assertDictEqual(r.__dict__, Review().get())

	@patch('feedparser.parse', return_value=feedparser.parse(os.path.abspath('assets/rss/default.rss')))
	def test_review_get_route(self, parser_function):
		expect = (Review()).get()
		response = self.app.get('/review')
		self.assertDictEqual(expect, response.json)
