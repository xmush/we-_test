import json
import config
import os
from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager, verify_jwt_in_request, get_jwt
from flask_script import Manager
from functools import wraps
from flask_orator import Orator

app = Flask(__name__)
jwt = JWTManager(app)
app.config['APP_DEBUG'] = True

def admin_required(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        verify_jwt_in_request()
        claims = get_jwt()
        if claims != "admin":
            return {'message': 'Unauthorize, Admin only'}, 401
        else:
            return fn(*args, **kwargs)
    return wrapper

flask_env = os.environ.get('FLASK_ENV', 'Development')
if flask_env == "Production":
    pass
    app.config.from_object(config.ProductionConfig)
elif flask_env == "Testing":
    pass
    app.config.from_object(config.TestingConfig)
else:
    app.config.from_object(config.DevelopmentConfig)

db = Orator(app)

@app.before_request
def before_request():
    if request.method != 'OPTIONS':  # <-- required
        pass
    else:
        return {}, 200, {'Access-Control-Allow-Origin': '*', 'Access-Control-Allow-Methods': 'POST, PATCH, GET, DELETE', 'Access-Control-Allow-Headers': '*'}


@app.after_request
def after_request(response):
    try:
        requestData = request.get_json()
    except Exception as e:
        requestData = request.args.to_dict()
    if response.status_code == 200:
        app.logger.warning("REQUEST_LOG\t%s",
                           json.dumps({
                               'method': request.method,
                               'code': response.status,
                               'uri': request.full_path,
                               'request': requestData,
                               'response': json.loads(response.data.decode('utf-8'))
                           })
                           )
    else:
        app.logger.error("REQUEST_LOG\t%s",
                         json.dumps({
                             'method': request.method,
                             'code': response.status,
                             'uri': request.full_path,
                             'request': requestData,
                             'response': json.loads(response.data.decode('utf-8'))
                         }))
    return response

from blueprints.hospital.resources import bp_hospital
app.register_blueprint(bp_hospital, url_prefix='/hospital')

# from blueprints.auth import bp_auth
# app.register_blueprint(bp_auth, url_prefix='/auth')

# from blueprints.user.resources import bp_user
# app.register_blueprint(bp_user, url_prefix='/user')
