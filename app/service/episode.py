from app.model import PodcastEpisodeModel
from app.app import db
import uuid
import datetime

class Episode():
	def getEpisode(self, episode_id) -> PodcastEpisodeModel:
		return PodcastEpisodeModel.query.filter_by(episode_id=episode_id).first()
	
	def setEpisode(self, username, args) -> PodcastEpisodeModel:
		episode = PodcastEpisodeModel(
			episode_id=str(uuid.uuid4()),
			episode_number=int(args['episode_number']),
			title=str(args['title']),
			description=str(args['description']),
			uri=str(args['uri']),
			published_date=datetime.datetime.now(),
			show_id=str(args['show_id'])
		)
		db.session.add(episode)
		db.session.commit()
		return episode
