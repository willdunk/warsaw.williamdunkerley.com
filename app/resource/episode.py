from flask_restx import Resource, Namespace, reqparse
from app.service import Episode as EpisodeService
from app.app import api
from app.utils import episode_fields
from flask_jwt_extended import jwt_required, get_jwt_identity

api = Namespace('episode', description="Episode operations")

parser = reqparse.RequestParser()
parser.add_argument('episode_number', help='This field cannot be blank', required=True, location="json")
parser.add_argument('title', help='This field cannot be blank', required=True, location="json")
parser.add_argument('description', help='This field cannot be blank', required=True, location="json")
parser.add_argument('uri', help='This field cannot be blank', required=True, location="json")
parser.add_argument('show_id', help='This field cannot be blank', required=True, location="json")

@api.route('/<string:episode_uuid>')
class Episode(Resource):
	@api.doc(security=None)
	@api.marshal_with(episode_fields)
	def get(self, episode_uuid):
		return EpisodeService().getEpisode(episode_uuid)

@api.route('')
class Episodes(Resource):
	@jwt_required()
	@api.expect(parser)
	@api.marshal_with(episode_fields)
	def post(self):
		return EpisodeService().setEpisode(get_jwt_identity(), parser.parse_args())
