from marshmallow import Schema, fields


class GenreSchema(Schema):
    id = fields.Integer(dump_only=True)
    name = fields.String()
