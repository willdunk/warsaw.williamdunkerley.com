import pytest

from app.app import db

@pytest.fixture
def session(request):
	"""Creates a session that's bound to a connection. See:
	http://alexmic.net/flask-sqlalchemy-pytest/
	"""
	# first, set up our connection-scoped session
	connection = db.engine.connect()
	transaction = connection.begin()

	options = dict(bind=connection, binds={})
	session = db.create_scoped_session(options=options)

	# this is how we're going to clean up
	def teardown():
		transaction.rollback()
		connection.close()
		session.remove()

	request.addfinalizer(teardown)

	# finally, use the session we made
	db.session = session
	return db.session
