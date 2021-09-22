from blueprints import db
from flask_restful import fields
from orator import SoftDeletes


class User(SoftDeletes, db.Model) :
    __fillable__ = ['name', 'password', 'email', 'role']

    __dates__ = ['deleted_at']

    response_fields ={
        'id' : fields.Integer,
        'name' : fields.String,
        'password' : fields.String,
        'email' : fields.String,
        'created_at' : fields.DateTime,
        'updated_at' : fields.DateTime,
        'deleted_at' : fields.DateTime
    }

    jwt_claims_fields = {
        'id' : fields.Integer,
        'email' : fields.String,
    }

    def __repr__(self) :
        return '<User %r>' % self.name