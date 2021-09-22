from blueprints import db
from flask_restful import fields


class Hospital(db.Model) :

    __table__ = 'hospital_list'

    __fillable__ = ['name', 'longitude', 'latitude', 'status']

    response_fields ={
        'id' : fields.Integer,
        'name' : fields.String,
        'longitude' : fields.Float,
        'latitude' : fields.Float,
        'status' : fields.Integer,
        'created_at' : fields.DateTime,
        'updated_at' : fields.DateTime,
    }

    def __repr__(self) :
        return '<Hospital %r>' % self.name