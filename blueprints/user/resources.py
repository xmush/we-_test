from flask import Blueprint
from flask_restful import Api, reqparse, Resource, marshal
from .model import User
from blueprints import app, admin_required
from flask_orator import  jsonify
import hashlib
from helper.encryption import Encryption
from flask_jwt_extended import jwt_required

bp_user = Blueprint('User', __name__)
api = Api(bp_user)

class UserResource(Resource) :
    def __init__(self) :
        pass

    @admin_required
    def get(self, id) :
        user = User.find(id)    
        app.logger.debug('DEBUG : %s', user)

        return marshal(user, User.response_fields), 200
        # return jsonify(user)

    def post(self) :
        parser = reqparse.RequestParser()
        parser.add_argument('name', location='json', required=True)
        parser.add_argument('password', location='json', required=True)
        parser.add_argument('email', location='json', required=True)       

        data = parser.parse_args()

        password_hash = Encryption.generatePassword(data['password'])
        
        try:
            user = User()
            user.name = data['name']
            user.password = password_hash
            user.email = data['email']
            user.role = 'user'
            user.save()

            app.logger.debug('DEBUG : %s', user)
            return marshal(user, User.response_fields), 200

        except Exception as e :
            app.logger.debug('DEBUG : %s', 'EROR'+str(e))
            return {'msg' : 'failed to save data'}, 500


    def patch(self, id) :
        parser = reqparse.RequestParser()
        parser.add_argument('name', location='json')
        data = parser.parse_args()

        user = User.find(id)
        user.name = data['name']
        user.save()

        return marshal(user, User.response_fields), 200

    def delete(self, id) :
        
        user = User.find(id)
        user.delete()
        return {'msg' : 'data successfuly deleted'}, 200

class UserResourceList(Resource) :
    def __init__(self) :
        pass

    @jwt_required
    def get(self) :
        users = User.all()

        app.logger.debug('DEBUG : %s', users)

        return jsonify(users)




api.add_resource(UserResourceList, '/list', '')
api.add_resource(UserResource, '', '/<id>')
