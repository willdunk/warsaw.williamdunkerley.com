from flask_restful import Resource
from app.app import api
from typing import List
from app.model import PodcastShowModel
from app.app import db

class Podcast():
	def getPodcasts(self) -> List[PodcastShowModel]:
		return PodcastShowModel.query.order_by(PodcastShowModel.title).all()

	def getPodcast(self, show_id) -> PodcastShowModel:
		return PodcastShowModel.query.filter_by(show_id=show_id).first()