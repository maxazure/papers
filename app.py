
from flask import Flask, jsonify, request, json
from flask_cors import CORS
from flask_bcrypt import Bcrypt
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity
from flask_migrate import Migrate

from werkzeug.exceptions import HTTPException, InternalServerError
from werkzeug.exceptions import default_exceptions

from config import app_config
from baseapi import BaseApi

config_name = 'development'
bcrypt = Bcrypt()

app = Flask(__name__,static_url_path='', 
            static_folder='static')
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
api = BaseApi(app, catch_all_404s=True)
app.config.from_object(app_config[config_name])
db = SQLAlchemy(app)
db.init_app(app)
migrate = Migrate(app, db)
jwt = JWTManager(app)
bcrypt.init_app(app)

from upload import upload_file
from front import index
from resourses.courses_resource import CoursesResource
from resourses.session.userinfo_resource import UserinfoResource
from resourses.session.login_resource import LoginResource
from resourses.keywords_resource import KeywordsResource
from resourses.papers_resource import PapersResource
from resourses.users_resource import UsersResource
from resourses.selects_resource import SelectsResource
# from utils.error_handle import *
# for ex in default_exceptions:
#     app.register_error_handler(ex, handle_error)

# front


api.prefix = '/api'
api.add_resource(LoginResource, '/auth/login')
api.add_resource(UserinfoResource, '/auth/userinfo')
api.add_resource(UsersResource, '/users', '/users/<int:user_id>')
api.add_resource(PapersResource, '/papers', '/papers/<int:paper_id>')
api.add_resource(KeywordsResource, '/keywords',
                 '/keywords/<int:keyword_id>')

api.add_resource(CoursesResource,  '/courses', '/courses/<int:course_id>')
api.add_resource(SelectsResource,  '/selects')

if __name__ == '__main__':
    app.run()
