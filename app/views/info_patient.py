import datetime

from app import db
from flask import request, jsonify

from ..enums.examRealizedEnum import ExamConfirmationEnum
from ..models.info_patient import InfoPatient, infoPatient_schema, infoPatients_schema
from ..enums.PregnantCodeEnum import PregnantCodeEnum
from sqlalchemy import desc

"""
def post_infoPatient():
    dt_notific = datetime.datetime.now()
    cs_gestant = request.json['cs_gestant']
    dt_invest = request.json['dt_invest']
    id_ocupa_n = request.json['id_ocupa_n']
    ant_uf_1 = request.json['ant_uf_1']
    mun_1 = request.json['mun_1']
    ant_uf_2 = request.json['ant_uf_2']
    mun_2 = request.json['mun_2']
    ant_uf_3 = request.json['ant_uf_3']
    mun_3 = request.json['mun_3']
    historia = request.json['historia']
    assintoma = request.json['assintoma']
    edema = request.json['edema']
    meningoe = request.json['meningoe']
    poliadeno = request.json['poliadeno']
    febre = request.json['febre']
    hepatome = request.json['hepatome']
    sinais_icc = request.json['sinais_icc']
    arritmias = request.json['arritmias']
    astenia = request.json['astenia']
    esplenom = request.json['esplenom']
    chagoma = request.json['chagoma']
    exame = request.json['exame']
    xenodiag = request.json['xenodiag']

    patient_id = request.json['patient_id']

    if patient_id:
        patient = get_patient_by_id(patient_id)
        if patient:
            cs_sexo = patient.sex
            dt_nasc = patient.dt_nasc
            sg_uf = patient.residenceUfId
            id_mn_resi = patient.residenceMunId
            cs_raca = request.json['cs_raca']
        else:
            return jsonify({'message': 'Paciente não existe.', 'data': {}}), 400
    else:
        return jsonify({'message': 'Id do paciente não informado.', 'data': {}}), 400

    infoPatient = InfoPatient(dt_notific, sg_uf, id_mn_resi, dt_nasc, cs_sexo, cs_gestant, cs_raca, dt_invest, id_ocupa_n, ant_uf_1,
                 mun_1, ant_uf_2, mun_2, ant_uf_3, mun_3, historia, assintoma, edema, meningoe, poliadeno, febre,
                 hepatome, sinais_icc, arritmias, astenia, esplenom, chagoma, exame, xenodiag)

    try:
        db.session.add(infoPatient)
        db.session.commit()
        result = infoPatient_schema.dump(infoPatient)
        return jsonify({'message': 'successfully registered', 'data': result}), 201
    except Exception as e:
        print(e)
        return jsonify({'message': 'unable to create', 'data': {}}), 500
"""


def update_info_patient(patient_id):
    resultRequest = request.get_json()
    print(resultRequest)
    visitMunicipio = resultRequest['visitMunicipio']
    visitEstado = resultRequest['visitEstado']

    print(visitMunicipio)
    visitMunicipio = sorted(visitMunicipio)
    print(visitMunicipio)

    print(visitEstado)
    visitEstado = sorted(visitEstado)
    print(visitEstado)
    countState = 0

    for stateId in visitEstado:
        if countState == 0:
            ant_uf_1 = stateId
        if countState == 1:
            ant_uf_2 = stateId
        if countState == 2:
            ant_uf_3 = stateId
        if countState == 3:
            break
        countState += 1

    countMun = 0
    for munId in visitMunicipio:
        if countMun == 0:
            mun_1 = munId
        if countMun == 1:
            mun_2 = munId
        if countMun == 2:
            mun_3 = munId
        if countMun == 3:
            break
        countMun += 1

    dt_notific = request.json['dt_notific']
    cs_gestant = request.json['cs_gestant']
    dt_invest = request.json['dt_invest']
    id_ocupa_n = request.json['id_ocupa_n']
    historia = request.json['historia']
    assintoma = request.json['assintoma']
    edema = request.json['edema']
    meningoe = request.json['meningoe']
    poliadeno = request.json['poliadeno']
    febre = request.json['febre']
    hepatome = request.json['hepatome']
    sinais_icc = request.json['sinais_icc']
    arritmias = request.json['arritmias']
    astenia = request.json['astenia']
    esplenom = request.json['esplenom']
    chagoma = request.json['chagoma']
    exame = request.json['exame']
    xenodiag = request.json['xenodiag']

    info_patient = InfoPatient.query.filter(InfoPatient.id_patient == patient_id).order_by(desc(InfoPatient.id)).one()

    if not info_patient:
        return jsonify({"message": "Consulta não existe", "data": {}})

    try:
        info_patient.dt_notific = dt_notific
        info_patient.cs_gestant = cs_gestant
        info_patient.dt_invest = dt_invest
        info_patient.id_ocupa_n = id_ocupa_n
        info_patient.ant_uf_1 = ant_uf_1
        info_patient.mun_1 = mun_1
        info_patient.ant_uf_2 = ant_uf_2
        info_patient.mun_2 = mun_2
        info_patient.ant_uf_3 = ant_uf_3
        info_patient.mun_3 = mun_3
        info_patient.historia = historia
        info_patient.assintoma = assintoma
        info_patient.edema = edema
        info_patient.meningoe = meningoe
        info_patient.poliadeno = poliadeno
        info_patient.febre = febre
        info_patient.hepatome = hepatome
        info_patient.sinais_icc = sinais_icc
        info_patient.arritmias = arritmias
        info_patient.astenia = astenia
        info_patient.esplenom = esplenom
        info_patient.chagoma = chagoma
        info_patient.exame = exame
        info_patient.xenodiag = xenodiag
        db.session.commit()
        result = infoPatient_schema.dump(info_patient)
        return jsonify({'message': 'successfully updated', 'data': result}), 200
    except Exception as e:
        print(e)
        return jsonify({'message': 'unable to update', 'data': {}}), 500


def insert_infoPatient(patient):
    dt_notific = datetime.datetime.now()
    cs_gestant = PregnantCodeEnum.IGNORED.value
    dt_invest = datetime.datetime.now()
    id_ocupa_n = 0
    ant_uf_1 = 10000
    mun_1 = 10000
    ant_uf_2 = 10000
    mun_2 = 10000
    ant_uf_3 = 10000
    mun_3 = 10000
    historia = ExamConfirmationEnum.IGNORED.value
    assintoma = ExamConfirmationEnum.IGNORED.value
    edema = ExamConfirmationEnum.IGNORED.value
    meningoe = ExamConfirmationEnum.IGNORED.value
    poliadeno = ExamConfirmationEnum.IGNORED.value
    febre = ExamConfirmationEnum.IGNORED.value
    hepatome = ExamConfirmationEnum.IGNORED.value
    sinais_icc = ExamConfirmationEnum.IGNORED.value
    arritmias = ExamConfirmationEnum.IGNORED.value
    astenia = ExamConfirmationEnum.IGNORED.value
    esplenom = ExamConfirmationEnum.IGNORED.value
    chagoma = ExamConfirmationEnum.IGNORED.value
    exame = ExamConfirmationEnum.IGNORED.value
    xenodiag = ExamConfirmationEnum.IGNORED.value
    cs_sexo = patient["sex"]
    dt_nasc = patient["dt_nasc"]
    sg_uf = patient["residenceUfId"]
    id_mn_resi = patient["residenceMunId"]
    cs_raca = patient["cs_raca"]
    patient_id = patient["id"]
    infoPatient = InfoPatient(dt_notific, sg_uf, id_mn_resi, dt_nasc, cs_sexo, cs_gestant, cs_raca, dt_invest, id_ocupa_n, ant_uf_1,
                 mun_1, ant_uf_2, mun_2, ant_uf_3, mun_3, historia, assintoma, edema, meningoe, poliadeno, febre,
                 hepatome, sinais_icc, arritmias, astenia, esplenom, chagoma, exame, xenodiag, patient_id)
    db.session.add(infoPatient)
    db.session.commit()
    return infoPatient_schema.dump(infoPatient)


def get_info_patients():
    users = InfoPatient.query.all()

    if users:
        result = infoPatients_schema.dump(users)
        return jsonify({"message": "success fetched", "data": result})

    return jsonify({"message": "nothing found", "data": {}})


def get_last_info_by_patient(patient_id):
    patient = InfoPatient.query.filter(InfoPatient.id_patient == patient_id).order_by(desc(InfoPatient.id)).one()

    if patient:
        result = infoPatients_schema.dump(patient)
        return jsonify({"message": "Consulta do paciente encontrado", "data": result})

    return jsonify({"message": "Consulta do Paciente não encontrado", "data": {}})
