from app.app import db
from .base import BaseModel

class PodcastEpisodeModel(BaseModel, db.Model):
	__tablename__ = 'podcast_episode'

	episode_id = db.Column(db.Text, primary_key=True)
	episode_number = db.Column(db.Integer)
	title = db.Column(db.Text)
	description = db.Column(db.Text)
	uri = db.Column(db.Text)
	published_date = db.Column(db.DateTime)
	show_id = db.Column(db.Text, db.ForeignKey('podcast_show.show_id'), nullable=False)
