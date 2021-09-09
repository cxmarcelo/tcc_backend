from app import db, ma


class Occupation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

    def __init__(self, state_id, name):
        self.id = state_id
        self.name = name


class OccupationSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name')


occupation_schema = OccupationSchema()
occupations_schema = OccupationSchema(many=True)
