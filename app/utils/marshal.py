from flask_restx import fields
from app.app import api
from werkzeug.http import HTTP_STATUS_CODES

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

user_fields = api.model('User', {
	'username': fields.String,
	'is_admin': fields.Boolean
})

both_tokens_fields = api.model('BothTokens', {
	'access_token': fields.String,
	'refresh_token': fields.String
})

access_token_fields = api.model('AccessToken', {
	'access_token': fields.String
})

generic_message_fields = api.model('GenericMessage', {
	'message': fields.String
})

error_fields = api.model('Error', {
	'message': fields.String
})

def possible_error(code):
	return {
		'code': code,
		'description': HTTP_STATUS_CODES.get(code),
		'model': error_fields,
	}
