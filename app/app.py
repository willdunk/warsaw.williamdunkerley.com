from flask import Flask, Blueprint, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_apscheduler import APScheduler 
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from flask_restx import Api
from werkzeug.middleware.proxy_fix import ProxyFix

authorizations = {
	'jwt': {
		'type': 'apiKey',
		'in': 'header',
		'name': 'Authorization',
		'description': "Type in the *'Value'* input box below: **'Bearer &lt;JWT&gt;'**, where JWT is the token"
	}
}

class PatchedApi(Api):
	@property
	def specs_url(self):
		return url_for(self.endpoint('specs'))

app = Flask(__name__, instance_relative_config=True)
CORS(app)

blueprint = Blueprint('api', __name__, url_prefix='/api/v1')
api = PatchedApi(blueprint, doc='/doc/', title="Warsaw", authorizations=authorizations, security='jwt')

app.register_blueprint(blueprint)

app.config.from_object('config')
app.config.from_envvar('APP_CONFIG_FILE')
app.config['JWT_BLACKLIST_ENABLED'] = True
app.config['JWT_BLACKLIST_TOKEN_CHECKS'] = ['access', 'refresh']
app.config['RESTX_MASK_SWAGGER'] = False

jwt = JWTManager(app)
db = SQLAlchemy(app)
scheduler = APScheduler()
scheduler.init_app(app)
scheduler.start()

from app.resource.review import api as review_ns
api.add_namespace(review_ns)

from app.resource.podcast import api as podcast_ns
api.add_namespace(podcast_ns)

from app.resource.episode import api as episode_ns
api.add_namespace(episode_ns)

from app.resource.user import api as user_ns
api.add_namespace(user_ns)
