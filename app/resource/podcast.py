from flask_restx import Resource, Namespace, reqparse
from app.service import Podcast as PodcastService
from app.app import api
from app.utils import podcast_fields
from flask_jwt_extended import jwt_required, get_jwt_identity

api = Namespace('podcast', description="Podcast operations")

parser = reqparse.RequestParser()
parser.add_argument('title', help='This field cannot be blank', required=True, location="json")
parser.add_argument('description', help='This field cannot be blank', required=True, location="json")

@api.route('')
class Podcasts(Resource):
	@api.doc(security=None)
	@api.marshal_with(podcast_fields)
	def get(self):
		return PodcastService().getPodcasts()
	
	@api.expect(parser)
	@api.marshal_with(podcast_fields)
	@jwt_required()
	def post(self):
		return PodcastService().setPodcast(get_jwt_identity(), parser.parse_args())

@api.route('/<string:show_uuid>')
class Podcast(Resource):
	@api.doc(security=None)
	@api.marshal_with(podcast_fields)
	def get(self, show_uuid):
		return PodcastService().getPodcast(show_uuid)
