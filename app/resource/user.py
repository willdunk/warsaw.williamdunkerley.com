from flask_restx import Resource, reqparse, marshal_with, Namespace, cors
from app.model import UserModel, RevokedTokenModel
from flask_jwt_extended import jwt_required, get_jwt_identity, get_jwt
from app.service import User as UserService
from app.utils import user_fields, both_tokens_fields, error_fields, access_token_fields, possible_error, generic_message_fields
from werkzeug.exceptions import Conflict

api = Namespace('user', description='User operations')
parser = reqparse.RequestParser()
parser.add_argument('username', help='This field cannot be blank', required=True, location="json")
parser.add_argument('password', help='This field cannot be blank', required=True, location="json")
parser.add_argument('is_admin', type=bool, required=False, location="json")

@api.route('/register')
class Register(Resource):
	@api.doc(security=None)
	@api.expect(parser)
	@api.marshal_with(both_tokens_fields, code=201)
	@api.response(**possible_error(409))
	def post(self):
		return UserService().register(parser.parse_args())


@api.route('/login')
class Login(Resource):
	@api.doc(security=None)
	@api.expect(parser)
	@api.marshal_with(both_tokens_fields)
	@api.response(**possible_error(401))
	@api.response(**possible_error(404))
	def post(self):
		return UserService().login(parser.parse_args())


@api.route('/info')
class Info(Resource):
	@cors.crossdomain(origin="*")
	@jwt_required
	@api.marshal_with(user_fields)
	@api.response(**possible_error(401))
	def get(self):
		return UserService().get(get_jwt_identity())


@api.route('/logout/access')
class LogoutAccess(Resource):
	@jwt_required
	@api.marshal_with(generic_message_fields)
	@api.response(**possible_error(401))
	def post(self):
		return UserService().logoutAccess(get_jwt())


@api.route('/token/refresh')
class TokenRefresh(Resource):
	@jwt_required(refresh=True)
	@api.marshal_with(access_token_fields)
	@api.response(**possible_error(401))
	def post(self):
		return UserService().tokenRefresh(get_jwt_identity())


@api.route('/logout/refresh')
class LogoutRefresh(Resource):
	@jwt_required(refresh=True)
	@api.marshal_with(generic_message_fields)
	@api.response(**possible_error(401))
	def post(self):
		return UserService().logoutRefresh(get_jwt())
