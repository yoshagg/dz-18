from marshmallow import Schema, fields


class DirectorSchema(Schema):
    id = fields.Integer(dump_only=True)
    name = fields.String()
