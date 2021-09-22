from flask import Blueprint
from flask_restful import Api, Resource, reqparse, marshal

from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required

import hashlib
from blueprints import app
from ..user.model import User

bp_auth = Blueprint('auth', __name__)
api = Api(bp_auth)

class CreateTokenResource(Resource):
    
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('email', location='json', required=True)
        parser.add_argument('password', location='json', required=True)
        args = parser.parse_args()

        qry_user = User.where('email', args['email']).first()

        if qry_user is not None:
            user_salt = app.config['APP_KEY']
            user_type = qry_user.role
            encoded = ('%s%s' % (args['password'], user_salt)).encode('utf-8')
            hash_pass = hashlib.sha512(encoded).hexdigest()
            
            if hash_pass == qry_user.password and qry_user.email == args['email'] :
                qry_user = marshal(qry_user, User.jwt_claims_fields)
                token = create_access_token( identity=qry_user, user_claims=user_type, fresh=True )

                return {'token': token}, 200

        return {'status': 'UNAUTHORIZED'}, 401


api.add_resource(CreateTokenResource, '')