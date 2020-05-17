import pytest
import unittest
import feedparser
from unittest.mock import MagicMock, Mock, patch, PropertyMock
import os
import requests_mock

from app.app import app
from app.model import ReviewModel as ReviewModel


def test_thing(session):
	review = ReviewModel(title='foo')
	session.add(review)
	session.commit()
	assert review.title == 'foo'
