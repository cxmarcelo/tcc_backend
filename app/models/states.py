from app import db, ma


class States(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    initials = db.Column(db.String(3), unique=True, nullable=False)

    def __init__(self, state_id, name, initials):
        self.id = state_id
        self.name = name
        self.initials = initials


class StatesSchema(ma.Schema):
    class Meta:
        fields = ('id', 'initials', 'name')


state_schema = StatesSchema()
states_schema = StatesSchema(many=True)
