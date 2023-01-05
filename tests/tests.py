import pytest
from unittest.mock import MagicMock

from models import Genre, Director, Movie

from views import \
    GenreIDView, GenreView,\
    DirectorIDView, DirectorView,\
    MovieIDView, MovieView


@pytest.fixture()
def genre_dao():
    genre_view_init = GenreView(None)
    genre_id_view_init = GenreIDView(None)

    genre_1 = Genre(id=1, name="asshole")
    genre_2 = Genre(id=2, name="elohssa")

    genre_view_init.get = MagicMock(return_value=[genre_1, genre_2])
    genre_id_view_init.get = MagicMock(return_value=genre_1)


@pytest.fixture()
def director_dao():
    director_view_init = DirectorView(None)
    director_id_view_init = DirectorIDView(None)

    director_1 = Director(id=1, name="billy")
    director_2 = Director(id=2, name="steve")

    director_view_init.get = MagicMock(return_value=[director_1, director_2])

    director_id_view_init.get = MagicMock(return_value=director_2)


@pytest.fixture()
def movie_dao():
    movie_view_init = MovieView(None)
    movie_id_view_init = MovieIDView(None)

    movie_1 = Movie(id=1, title="kolenval")
    movie_2 = Movie(id=2, title="trackoboyshiks")

    movie_view_init.get = MagicMock(return_value=[movie_1, movie_2])
    movie_view_init.post = MagicMock(return_value=movie_1)

    movie_id_view_init.get = MagicMock(return_value=movie_2)
    movie_id_view_init.delete = MagicMock(return_value=True)
    movie_id_view_init.put = MagicMock(return_value=True)


class TestGenreService:
    @pytest.fixture(autouse=True)
    def genre_service(self, genre_dao):
        self.genre_view = GenreView(genre_dao)
        self.genre_id_view = GenreIDView(genre_dao)

    def test_get_genre_view(self):
        assert self.genre_view.get() is not None
        assert len(self.genre_view.get()) == 2

    def test_get_genre_id_view(self):
        assert self.genre_id_view.get(1) is not None
        assert self.genre_id_view.get(1).name == "asshole"


class TestDirectorService:
    @pytest.fixture(autouse=True)
    def director_service(self, director_dao):
        self.director_view = DirectorView(director_dao)
        self.director_id_view = DirectorIDView(director_dao)

    def test_get_director_view(self):
        assert self.director_view.get() is not None
        assert len(self.director_view.get()) == 2

    def test_get_director_id_view(self):
        assert self.director_id_view.get(1) is not None
        assert self.director_id_view.get(1).name == "billy"


class TestMovieService:
    @pytest.fixture(autouse=True)
    def movie_service(self, movie_dao):
        self.movie_view = MovieView(movie_dao)
        self.movie_id_view = MovieIDView(movie_dao)

    def test_get_movie_view(self):
        assert self.movie_view.get() is not None
        assert len(self.movie_view.get()) == 2

    def test_post_movie_view(self):
        assert self.movie_id_view.get(1) is not None
        assert self.movie_id_view.get(1).name == "kolenval"


## Как протестировать функции put delete и прочее, если они возвращают пустую строку, не имею представления
## Говорили ведь, что можно использовать и easy архитектуру для этого задания
















