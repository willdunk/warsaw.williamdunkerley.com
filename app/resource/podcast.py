from flask_restx import Resource, Namespace, reqparse
from app.service import Podcast as PodcastService
from app.app import api
from app.utils import podcast_fields

api = Namespace('podcast', description="Podcast operations")

parser = reqparse.RequestParser()
parser.add_argument('title', help='This field cannot be blank', required=True)
parser.add_argument('description', help='This field cannot be blank', required=True)

@api.route('')
class Podcasts(Resource):
	@api.marshal_with(podcast_fields)
	def get(self):
		return PodcastService().getPodcasts()
	
	@api.expect(parser)
	@api.marshal_with(podcast_fields)
	def post(self):
		return PodcastService().setPodcast(parser.parse_args())

@api.route('/<string:show_uuid>')
class Podcast(Resource):
	@api.marshal_with(podcast_fields)
	def get(self, show_uuid):
		return PodcastService().getPodcast(show_uuid)
