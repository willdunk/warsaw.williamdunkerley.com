import pytest
import unittest
import feedparser
from unittest.mock import MagicMock, Mock, patch, PropertyMock
import os
import requests_mock

from app.app import app
from app.service import Review as ReviewService

RSS_PATH = os.path.abspath('assets/rss/default.rss')

class TestReview(unittest.TestCase):
	def setUp(self): 
		self.app = app.test_client()

	def test_review_get_reviews_exists(self):
		# self.assertIsNotNone(ReviewService().getReviews)
		pass