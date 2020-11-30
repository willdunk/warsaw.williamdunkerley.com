from flask_restx import fields
from app.app import api

review_fields = api.model('Review', {
	'review_id': fields.String,
	'title': fields.String,
	'rating': fields.Integer,
	'review_link': fields.String,
	'movie_link': fields.String,
	'banner_image_link': fields.String,
	'content': fields.String,
	'published_date': fields.DateTime(dt_format='rfc822'),
	'watched_date': fields.DateTime(dt_format='rfc822'),
})

episode_fields = api.model('Episode', {
	'episode_id': fields.String,
	'episode_number': fields.Integer,
	'title': fields.String,
	'description': fields.String,
	'uri': fields.String,
	'published_date': fields.DateTime(dt_format='rfc822'),
	'show_id': fields.String,
})

podcast_fields = api.model('Podcast', {
	'show_id': fields.String,
	'title': fields.String,
	'description': fields.String,
	'episodes': fields.List(fields.Nested(episode_fields)),
})
