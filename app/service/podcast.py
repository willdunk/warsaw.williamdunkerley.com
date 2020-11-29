from app.app import db
from typing import List
from app.model import PodcastShowModel

class Podcast():
	def getPodcasts(self) -> List[PodcastShowModel]:
		return PodcastShowModel.query.order_by(PodcastShowModel.title).all()

	def getPodcast(self, show_id) -> PodcastShowModel:
		return PodcastShowModel.query.filter_by(show_id=show_id).first()

	def setPodcast(self, args) -> PodcastShowModel:
		podcast = PodcastShowModel(
			show_id=str(uuid.uuid4()),
			title=str(args['title']),
			description=str(args['description'])
		)
		db.session.add(podcast)
		db.session.commit()
		return podcast
