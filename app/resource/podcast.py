from flask_restful import Resource, fields, marshal_with
from app.service import Podcast as PodcastService
from app.app import api

episode_fields = {
	'episode_id': fields.String,
	'episode_number': fields.Integer,
	'title': fields.String,
	'description': fields.String,
	'uri': fields.String,
	'published_date': fields.DateTime(dt_format='rfc822'),
	'show_id': fields.String,
}

podcast_fields = {
	'show_id': fields.String,
	'title': fields.String,
	'description': fields.String,
	'episodes': fields.List(fields.Nested(episode_fields)),
}

class Podcast(Resource):
	def __init__(self):
		self.service = PodcastService()

	@marshal_with(podcast_fields)
	def get(self, show_id=None):
		if show_id is None:
			return self.service.getPodcasts()
		return self.service.getPodcast(show_id)
