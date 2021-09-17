from app import db, ma


class Patient(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(150), nullable=False)
    sex = db.Column(db.String(1))
    dt_nasc = db.Column(db.DateTime, nullable=False)
    cpfOrRg: db.Column(db.String(15), nullable=False, unique=True)
    residenceUfId = db.Column(db.Integer, nullable=False)
    residenceMunId = db.Column(db.Integer, nullable=False)

    def __init__(self, name, sex, dt_nasc, cpf_or_rg, residence_uf_id, residence_mun_id):
        self.name = name
        self.sex = sex
        self.dt_nasc = dt_nasc
        self.cpfOrRg = cpf_or_rg
        self.residenceUfId = residence_uf_id
        self.residenceMunId = residence_mun_id


class PatientSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'sex', 'dt_nasc', 'cpfOrRg', 'residenceUfId', 'residenceMunId')


patient_schema = PatientSchema()
patients_schema = PatientSchema(many=True)
