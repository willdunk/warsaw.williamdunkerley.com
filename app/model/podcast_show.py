from app.app import app, db
from .base import BaseModel

class PodcastShowModel(BaseModel, db.Model):
	__tablename__ = 'podcast_show'

	show_id = db.Column(db.Text, primary_key=True)
	title = db.Column(db.Text)
	description = db.Column(db.Text)
	episodes = db.relationship('PodcastEpisodeModel', backref='podcast_show', lazy=True)
