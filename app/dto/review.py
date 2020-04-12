class Review():
	def __init__(
		self,
		content=None,
		filmTitle=None,
		filmYear=None,
		memberRating=None,
		link=None
	):
		self.content = content
		self.filmTitle = filmTitle
		self.filmYear = filmYear
		self.memberRating = memberRating
		self.link = link
	
	def __eq__(self, other):
		"""Overrides the default implementation"""
		if isinstance(other, Review):
			return (
				self.content == other.content and 
				self.filmTitle == other.filmTitle and
				self.filmYear == other.filmYear and
				self.memberRating == other.memberRating and
				self.link == other.link
			)
		return False
