import pytest
import unittest
import json

from app import app
from app.views.review import Review

class ReviewTest(unittest.TestCase):
	def setUp(self): 
		self.app = app.test_client()

	def test_review_get_class(self):
		r = Review()
		expect = {"text": "text"}
		self.assertDictEqual(expect, r.get())

	def test_review_get_route(self):
		expect = (Review()).get()
		response = self.app.get('/review')
		self.assertDictEqual(expect, response.json)
		