from flask_restx import Resource, Namespace
from models import Genre, GenreSchema

genre_ns = Namespace('genre')


@genre_ns.route('/')
class GenreView(Resource):
    def get(self):
        data = Genre.query.all()
        return GenreSchema(many=True).dump(data), 200


@genre_ns.route('/<int:gid>')
class GenreIDView(Resource):
    def get(self, gid):
        genre = Genre.query.get(gid)
        return GenreSchema().dump(genre), 200
