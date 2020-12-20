from flask_restx import Resource, reqparse, marshal_with, Namespace, cors
from app.model import UserModel, RevokedTokenModel
from flask_jwt_extended import jwt_required, jwt_refresh_token_required, get_jwt_identity
from app.service import User as UserService
from app.utils import user_fields

api = Namespace('user', description='User operations', decorators=[cors.crossdomain(origin="*")])
parser = reqparse.RequestParser()
parser.add_argument('username', help='This field cannot be blank', required=True, location="json")
parser.add_argument('password', help='This field cannot be blank', required=True, location="json")
parser.add_argument('is_admin', required=False, location="json")


@api.route('/register')
class Register(Resource):
	@cors.crossdomain(origin="*")
	@api.doc(security=None)
	@api.expect(parser)
	def post(self):
		return UserService().register(parser.parse_args())


@api.route('/login')
class Login(Resource):
	@cors.crossdomain(origin="*")
	@api.doc(security=None)
	@api.expect(parser)
	def post(self):
		return UserService().login(parser.parse_args())


@api.route('/info')
class Info(Resource):
	@cors.crossdomain(origin="*")
	@jwt_required
	@api.marshal_with(user_fields)
	def get(self):
		return UserService().get(get_jwt_identity())


@api.route('/logout/access')
class LogoutAccess(Resource):
	@jwt_required
	def post(self):
		return UserService().logoutAccess(get_raw_jwt())


@api.route('/token/refresh')
class TokenRefresh(Resource):
	@jwt_refresh_token_required
	def post(self):
		return UserService().tokenRefresh(get_jwt_identity())


@api.route('/logout/refresh')
class LogoutRefresh(Resource):
	@jwt_refresh_token_required
	def post(self):
		return UserService().logoutRefresh(get_raw_jwt())
