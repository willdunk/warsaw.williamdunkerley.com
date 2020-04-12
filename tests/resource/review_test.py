import pytest
import unittest
import json
import feedparser
from unittest.mock import MagicMock, patch
import os

from app.app import app
from app.resource import Review as ReviewResource
from app.service import Review as ReviewService
from app.dto import Review as ReviewDto

RSS_PATH = os.path.abspath('assets/rss/default.rss')

class TestReview(unittest.TestCase):
	def setUp(self): 
		self.app = app.test_client()

	def test_review_get_method_exists(self):
		self.assertIsNotNone(ReviewResource().get)

	@patch('app.resource.Review.get', return_value=[{"mock":"mock"}])
	def test_review_get_route(self, get_func):
		expect = [{"mock":"mock"}]
		response = self.app.get('/review')
		self.assertListEqual(expect, response.json)

	@patch('app.resource.Review.get', return_value={"mock":"mock"})
	def test_review_get_index_route(self, get_func):
		index = 0
		expect = {"mock":"mock"}
		response = self.app.get(f'/review/{index}')
		self.assertDictEqual(expect, response.json)
		get_func.called_once_with(index)

	@patch('app.service.Review.getReviews', return_value=[ReviewDto("content1"), ReviewDto("content2")])
	def test_review_get_returns_list_dicts(self, service_func):
		expect = [ReviewDto("content1").__dict__, ReviewDto("content2").__dict__]
		self.assertListEqual(ReviewResource().get(), expect)

	@patch('app.service.Review.getReview', return_value=ReviewDto("content1"))
	def test_review_get_index_returns_dicts(self, service_func):
		index = 1
		expect = ReviewDto("content1").__dict__
		self.assertDictEqual(ReviewResource().get(index), expect)
		service_func.called_once_with(1)