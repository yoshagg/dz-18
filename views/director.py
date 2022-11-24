from flask_restx import Resource, Namespace
from models import Director, DirectorSchema

director_ns = Namespace('director')


@director_ns.route('/')
class DirectorView(Resource):
    def get(self):
        data = Director.query.all()
        result = []
        for d in data:
            sm_d = d.__dict__
            del sm_d['_sa_instance_state']
            result.append(sm_d)
        return DirectorSchema.dump(result), 200


@director_ns.route('/<int:did>')
class DirectorView(Resource):
    def get(self, did):
        director = Director.query.get(did)
        sm_d = director.__dict__
        del sm_d['_sa_instance_state']
        return DirectorSchema.dump(sm_d), 200
