from flask_restful import Resource, fields, marshal_with
from app.service import Episode as EpisodeService
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

class Episode(Resource):
	def __init__(self):
		self.service = EpisodeService()

	@marshal_with(episode_fields)
	def get(self, episode_id):
		return self.service.getEpisode(episode_id)
