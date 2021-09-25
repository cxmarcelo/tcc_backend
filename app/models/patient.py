from app import db, ma


class Patient(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(150), nullable=False)
    sex = db.Column(db.String(1), nullable=False)
    cs_raca = db.Column(db.Integer, nullable=False)
    dt_nasc = db.Column(db.Date, nullable=False)
    cpf = db.Column(db.String(15), nullable=False, unique=True)
    residenceUfId = db.Column(db.Integer, db.ForeignKey('states.id'), nullable=False)
    residenceMunId = db.Column(db.Integer, db.ForeignKey('counties.id'), nullable=False)
    state = db.relationship('States', backref='patient', lazy=True)

    def __init__(self, name, sex, cs_raca, dt_nasc, cpf, residence_uf_id, residence_mun_id):
        self.name = name
        self.sex = sex
        self.cs_raca = cs_raca
        self.dt_nasc = dt_nasc
        self.cpf = cpf
        self.residenceUfId = residence_uf_id
        self.residenceMunId = residence_mun_id


class PatientSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'sex', 'cs_raca', 'dt_nasc',
                  'cpf', 'residenceUfId', 'residenceMunId', 'state')


patient_schema = PatientSchema()
patients_schema = PatientSchema(many=True)
