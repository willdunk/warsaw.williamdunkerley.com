from typing import List
from app.model import UserModel, RevokedTokenModel
from app.app import db
from passlib.hash import pbkdf2_sha256 as sha256
from flask_jwt_extended import create_access_token, create_refresh_token, get_raw_jwt, get_jwt_identity
from flask_restx import abort

class User():
	def register(self, data):
		username = data['username']
		password = data['password']
		is_admin = data['is_admin']
		if UserModel.query.filter_by(username=username).first():
			abort(409, 'User {} already exists'.format(username))

		new_user = UserModel(
			username=data['username'],
			password=sha256.hash(password),
			is_admin=data['is_admin']
		)

		try:
			db.session.add(new_user)
			db.session.commit()
			access_token = create_access_token(identity=username)
			refresh_token = create_refresh_token(identity=username)
			return {
				'access_token': access_token,
				'refresh_token': refresh_token
			}
		except:
			abort(500)

	def get(self, username) -> UserModel:
		return UserModel.query.filter_by(username=username).first()

	def login(self, data):
		username = data['username']
		password = data['password']
		current_user = UserModel.query.filter_by(username=username).first()

		if not current_user:
			abort(404, 'User {} doesn\'t exist'.format(username))

		if sha256.verify(password, current_user.password):
			access_token = create_access_token(identity=username)
			refresh_token = create_refresh_token(identity=username)
			return {
				'access_token': access_token,
				'refresh_token': refresh_token
			}
		else:
			abort(401, 'Wrong Credentials')

	def logoutAccess(self, jwt):
		jti = jwt['jti']
		try:
			revoked_token = RevokedTokenModel(jti=jti)
			db.session.add(revoked_token)
			db.session.commit()
			return {'message': 'Access token has been revoked'}
		except:
			abort(500)

	def logoutRefresh(self, jwt):
		jti = jwt['jti']
		try:
			revoked_token = RevokedTokenModel(jti=jti)
			db.session.add(revoked_token)
			db.session.commit()
			return {'message': 'Refresh token has been revoked'}
		except:
			abort(500)

	def tokenRefresh(self, username):
		current_user = get_jwt_identity()
		access_token = create_access_token(identity=current_user)
		return {'access_token': access_token}
