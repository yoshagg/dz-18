from flask_restx import Resource, Namespace
from flask import request
from models import Movie
from setup_db import db
from models.schemas import MovieSchema

movie_ns = Namespace('movie')


@movie_ns.route('/')
class MovieView(Resource):
    def get(self):
        director_id = request.args.get("director_id")
        genre_id = request.args.get("genre_id")
        year = request.args.get("year")
        query = Movie.query
        if director_id is not None:
            query = query.filter(Movie.director_id == director_id)
        if genre_id is not None:
            query = query.filter(Movie.genre_id == genre_id)
        if year is not None:
            query = query.filter(Movie.year == year)
        return MovieSchema(many=True).dump(query.all()), 200

    def post(self):
        req_json = request.json
        ent = Movie(**req_json)
        db.session.add(ent)
        db.session.commit()
        return "", 201


@movie_ns.route('/<int:mid>')
class MovieIDView(Resource):
    def get(self, mid):
        movie = Movie.query.get(mid)
        return MovieSchema().dump(movie), 200

    def put(self, mid):
        movie = Movie.query.get(mid)
        req_json = request.json
        movie.title = req_json.get('title')
        movie.description = req_json.get('description')
        movie.trailer = req_json.get('trailer')
        movie.year = req_json.get('year')
        movie.rating = req_json.get('rating')
        movie.genre_id = req_json.get('genre_id')
        movie.director_id = req_json.get('director_id')

        db.session.add(movie)
        db.session.commit()
        return "", 204

    def delete(self, mid):
        movie = Movie.query.get(mid)

        db.session.delete(movie)
        db.session.commit()
        return "", 204
