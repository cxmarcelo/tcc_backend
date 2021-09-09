from app import db, ma


class Counties(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    uf_id = db.Column(db.Integer, db.ForeignKey('states.id'), nullable=False)
    state = db.relationship('States')
    # state = db.relationship('States', back_populates='')

    def __init__(self, county_id, name, uf_id):
        self.id = county_id
        self.name = name
        self.uf_id = uf_id


class CountiesSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'uf_id')


county_schema = CountiesSchema()
counties_schema = CountiesSchema(many=True)
