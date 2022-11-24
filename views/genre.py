from flask_restx import Resource, Namespace
from models import Genre, GenreSchema

genre_ns = Namespace('genre')


@genre_ns.route('/')
class GenreView(Resource):
    def get(self):
        data = Genre.query.all()
        result = []
        for d in data:
            sm_d = d.__dict__
            del sm_d['_sa_instance_state']
            result.append(sm_d)
        return GenreSchema.dump(result), 200


@genre_ns.route('/<int:gid>')
class GenreView(Resource):
    def get(self, gid):
        genre = Genre.query.get(gid)
        sm_d = genre.__dict__
        del sm_d['_sa_instance_state']
        return GenreSchema.dump(sm_d), 200
