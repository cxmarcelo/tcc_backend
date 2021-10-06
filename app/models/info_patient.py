from app import db, ma


class InfoPatient(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    dt_notific = db.Column(db.DateTime, nullable=False)
    sg_uf = db.Column(db.Integer, nullable=False)
    id_mn_resi = db.Column(db.Integer, nullable=False)
    dt_nasc = db.Column(db.DateTime, nullable=False)
    cs_sexo = db.Column(db.String(1))
    cs_gestant = db.Column(db.Integer, nullable=False)
    cs_raca = db.Column(db.Integer, nullable=False)
    dt_invest = db.Column(db.Date)
    id_ocupa_n = db.Column(db.Integer)
    ant_uf_1 = db.Column(db.Integer)
    mun_1 = db.Column(db.Integer)
    ant_uf_2 = db.Column(db.Integer)
    mun_2 = db.Column(db.Integer)
    ant_uf_3 = db.Column(db.Integer)
    mun_3 = db.Column(db.Integer)
    historia = db.Column(db.Integer)
    assintoma = db.Column(db.Integer)
    edema = db.Column(db.Integer)
    meningoe = db.Column(db.Integer)
    poliadeno = db.Column(db.Integer)
    febre = db.Column(db.Integer)
    hepatome = db.Column(db.Integer)
    sinais_icc = db.Column(db.Integer)
    arritmias = db.Column(db.Integer)
    astenia = db.Column(db.Integer)
    esplenom = db.Column(db.Integer)
    chagoma = db.Column(db.Integer)
    exame = db.Column(db.Integer)
    xenodiag = db.Column(db.Integer)
    id_patient = db.Column(db.Integer, db.ForeignKey('patient.id'), unique=True)
    patient = db.relationship('Patient')
    classi_fin = db.Column(db.Integer)

    def __init__(self, dt_notific, sg_uf, id_mn_resi, dt_nasc, cs_sexo, cs_gestant, cs_raca, dt_invest, id_ocupa_n, ant_uf_1,
                 mun_1, ant_uf_2, mun_2, ant_uf_3, mun_3, historia, assintoma, edema, meningoe, poliadeno, febre,
                 hepatome, sinais_icc, arritmias, astenia, esplenom, chagoma, exame, xenodiag, id_patient, classi_fin):
        self.dt_notific = dt_notific
        self.sg_uf = sg_uf
        self.id_mn_resi = id_mn_resi
        self.dt_nasc = dt_nasc
        self.cs_sexo = cs_sexo
        self.cs_gestant = cs_gestant
        self.cs_raca = cs_raca
        self.dt_invest = dt_invest
        self.id_ocupa_n = id_ocupa_n
        self.ant_uf_1 = ant_uf_1
        self.mun_1 = mun_1
        self.ant_uf_2 = ant_uf_2
        self.mun_2 = mun_2
        self.ant_uf_3 = ant_uf_3
        self.mun_3 = mun_3
        self.historia = historia
        self.assintoma = assintoma
        self.edema = edema
        self.meningoe = meningoe
        self.poliadeno = poliadeno
        self.febre = febre
        self.hepatome = hepatome
        self.sinais_icc = sinais_icc
        self.arritmias = arritmias
        self.astenia = astenia
        self.esplenom = esplenom
        self.chagoma = chagoma
        self.exame = exame
        self.xenodiag = xenodiag
        self.id_patient = id_patient
        self.classi_fin = classi_fin


class InfoPatientSchema(ma.Schema):
    class Meta:
        fields = ('dt_notific', 'sg_uf', 'id_mn_resi', 'dt_nasc', 'cs_sexo', 'cs_gestant', 'cs_raca', 'dt_invest', 'id_ocupa_n', 'ant_uf_1',
                 'mun_1', 'ant_uf_2', 'mun_2', 'ant_uf_3', 'mun_3', 'historia', 'assintoma', 'edema', 'meningoe', 'poliadeno', 'febre',
                 'hepatome', 'sinais_icc', 'arritmias', 'astenia', 'esplenom', 'chagoma', 'exame', 'xenodiag', 'res_hist', 'id_patient',
                  'classi_fin')


infoPatient_schema = InfoPatientSchema()
infoPatients_schema = InfoPatientSchema(many=True)
