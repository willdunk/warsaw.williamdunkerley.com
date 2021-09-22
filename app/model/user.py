from app.app import db, jwt
from .base import BaseModel

class UserModel(BaseModel, db.Model):
	__tablename__ = 'warsaw_user'

	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(120), unique=True, nullable=False)
	password = db.Column(db.String(120), nullable=False)
	is_admin = db.Column(db.Boolean)

class RevokedTokenModel(BaseModel, db.Model):
	__tablename__ = 'revoked_token'
	id = db.Column(db.Integer, primary_key=True)
	jti = db.Column(db.String(120))

# @jwt.token_in_blacklist_loader
# def check_if_token_in_blacklist(decrypted_token):
# 	jti = decrypted_token['jti']
# 	return bool(RevokedTokenModel.query.filter_by(jti=jti).first())
