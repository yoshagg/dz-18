from flask import Flask
from flask_restx import Api

from config import Config
from setup_db import db
from models import Director, Genre, Movie
from views.movie import movie_ns
from views.genre import genre_ns
from views.director import director_ns


def create_app(config_object):
    app = Flask(__name__)
    app.config.from_object(config_object)
    register_extensions(app)
    return app


def register_extensions(app):
    db.init_app(app)
    api = Api(app)
    api.add_namespace(movie_ns)
    api.add_namespace(genre_ns)
    api.add_namespace(director_ns)
    create_data(app, db)


def create_data(app, db):
    with app.app_context():
        db.create_all()
        ass_movie = Movie(title="ASS", description="ass we can", trailer="foo", year=2288, rating=11.5, genre_id=1, director_id=1)
        arthouse = Genre(name="Arthouse")
        billy_harrington = Director(name="Billy Harrington")

        with db.session.begin():
            db.session.add_all([ass_movie, arthouse, billy_harrington])


config = Config()
app = create_app(config)
app.debug = True

if __name__ == '__main__':
    app.run(host="localhost", port=10001, debug=True)
