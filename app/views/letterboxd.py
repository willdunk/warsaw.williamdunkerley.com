from flask_restful import Resource

class Letterboxd(Resource):
	def get(self):
		return {'hello': "there"}
