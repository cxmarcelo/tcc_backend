import datetime

from werkzeug.security import generate_password_hash
from app import db
from flask import request, jsonify
from ..models.info_patient import InfoPatient, infoPatient_schema, infoPatients_schema
from .patient import get_patient_by_id


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
    res_hist = request.json['res_hist']

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
                 hepatome, sinais_icc, arritmias, astenia, esplenom, chagoma, exame, xenodiag, res_hist)

    try:
        db.session.add(infoPatient)
        db.session.commit()
        result = infoPatient_schema.dump(infoPatient)
        return jsonify({'message': 'successfully registered', 'data': result}), 201
    except Exception as e:
        print(e)
        return jsonify({'message': 'unable to create', 'data': {}}), 500


def update_user(user_id):
    username = request.json['username']
    password = request.json['password']
    name = request.json['name']
    email = request.json['email']

    user = InfoPatient.query.get(user_id)

    if not user:
        return jsonify({"message": "User don't exist", "data": {}})

    pass_hash = generate_password_hash(password)

    try:
        user.username = username
        user.password = pass_hash
        user.name = name
        user.email = email
        db.session.commit()
        result = infoPatient_schema.dump(user)
        return jsonify({'message': 'successfully updated', 'data': result}), 200
    except Exception as e:
        print(e)
        return jsonify({'message': 'unable to update', 'data': {}}), 500


def get_users():
    users = InfoPatient.query.all()

    if users:
        result = infoPatients_schema.dump(users)
        return jsonify({"message": "success fetched", "data": result})

    return jsonify({"message": "nothing found", "data": {}})


def get_user(user_id):
    user = InfoPatient.query.get(user_id)

    if user:
        result = infoPatient_schema.dump(user)
        return jsonify({"message": "success fetched", "data": result}), 200

    return jsonify({"message": "user don't exist", "data": {}}), 404


def delete_user(user_id):
    user = InfoPatient.query.get(user_id)
    try:
        db.session.delete(user)
        db.session.commit()
        result = infoPatient_schema.dump(user)
        return jsonify({"message": "successfully deleted", "data": result}), 200
    except Exception as e:
        print(e)
        return jsonify({"message": "unable to delete", "data": {}}), 500


def counties_by_ufId(uf_id):
    name = request.args.get('name')
    print(name)
    counties = InfoPatient.query.filter(InfoPatient.uf_id == uf_id).filter(InfoPatient.name.like(f'{name}%'))

    if counties:
        result = infoPatients_schema.dump(counties)
        return jsonify({"message": "success fetched", "data": result})

    return jsonify({"message": "nothing found", "data": {}})
