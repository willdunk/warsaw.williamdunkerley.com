from flask_restful import Resource
from app.app import api
from app.model import PodcastEpisodeModel
from app.app import db

class Episode():
	def getEpisode(self, episode_id) -> PodcastEpisodeModel:
		return PodcastEpisodeModel.query.filter_by(episode_id=episode_id).first()
