from flask_restful import Resource, fields, marshal_with, reqparse
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

	@marshal_with(episode_fields)
	def post(self):
		parse = reqparse.RequestParser()
		parse.add_argument('episode_number')
		parse.add_argument('title')
		parse.add_argument('description')
		parse.add_argument('uri')
		parse.add_argument('show_id')
		args = parse.parse_args()
		return self.service.setEpisode(args)
