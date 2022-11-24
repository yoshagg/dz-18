from marshmallow import Schema, fields
from models.schemas.director_schema import DirectorSchema
from models.schemas.genre_schema import GenreSchema


class MovieSchema(Schema):
    id = fields.Integer(dump_only=True)
    title = fields.String()
    description = fields.String()
    trailer = fields.String()
    year = fields.Integer()
    rating = fields.Float()
    genre = fields.Nested(GenreSchema)
    director = fields.Nested(DirectorSchema)
