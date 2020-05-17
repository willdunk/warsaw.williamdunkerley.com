import pytest
import unittest
from unittest.mock import MagicMock, patch
import uuid
from collections import OrderedDict

from app.app import app
from app.resource import Review as ReviewResource
from app.service import Review as ReviewService
from app.model import ReviewModel

default_review = {
	'review_id': 'review_id',
	'title': 'title',
	'rating': 10,
	'review_link': 'review_link',
	'movie_link': 'movie_link',
	'banner_image_link': 'banner_image_link',
	'content': 'content'
}

class TestReview(unittest.TestCase):
	def setUp(self): 
		self.app = app.test_client()

	def test_review_get_method_exists(self):
		self.assertIsNotNone(ReviewResource().get)

	@patch('app.resource.Review.get', return_value=[{"mock": "mock"}])
	def test_review_get_route(self, get_func):
		expect = [{"mock":"mock"}]
		response = self.app.get('/review')
		self.assertListEqual(expect, response.json)

	@patch('app.resource.Review.get', return_value={"mock":"mock"})
	def test_review_get_index_route(self, get_func):
		index = str(uuid.uuid4())
		expect = {"mock":"mock"}
		response = self.app.get(f'/review/{index}')
		self.assertDictEqual(expect, response.json)
		get_func.called_once_with(index)

	@patch('app.service.Review.getReviews', return_value=[default_review])
	def test_review_get_returns_list(self, service_func):
		expect = [default_review]
		self.assertListEqual(ReviewResource().get(), expect)

	@patch('app.service.Review.getReview', return_value=default_review)
	def test_review_get_index_returns_fields(self, service_func):
		index = 1
		expect = default_review
		self.assertDictEqual(ReviewResource().get(index), expect)
		service_func.called_once_with(1)
