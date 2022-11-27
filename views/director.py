from flask_restx import Resource, Namespace
from models import Director, DirectorSchema

director_ns = Namespace('director')


@director_ns.route('/')
class DirectorView(Resource):
    def get(self):
        data = Director.query.all()
        return DirectorSchema(many=True).dump(data), 200


@director_ns.route('/<int:did>')
class DirectorView(Resource):
    def get(self, did):
        director = Director.query.get(did)
        return DirectorSchema().dump(director), 200
