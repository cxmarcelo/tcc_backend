from app import db
from flask import request, jsonify
from ..models.patient import Patient, patient_schema, patients_schema
from ..models.states import States, state_schema
from ..models.counties import Counties, county_schema
from ..models.info_patient import InfoPatient, infoPatient_schema
from .info_patient import insert_infoPatient, get_result


def post_patient():
    name = request.json['name']
    sex = request.json['sex']
    cs_raca = request.json['cs_raca']
    dt_nasc = request.json['dt_nasc']
    cpf = request.json['cpf']
    residenceUfId = request.json['residenceUfId']
    residenceMunId = request.json['residenceMunId']

    patient = Patient(name, sex, cs_raca, dt_nasc, cpf, residenceUfId, residenceMunId)

    try:
        db.session.add(patient)
        db.session.commit()
        resultPatient = patient_schema.dump(patient)
        resultInfoPatient = insert_infoPatient(resultPatient)

        obj = {"patient": resultPatient, "resultInfoPatient": resultInfoPatient}
        return jsonify({'message': 'Paciente Criado.', 'data': obj}), 201

    except Exception as e:
        print(e)
        return jsonify({'message': 'Falha ao criar paciente.', 'data': {}}), 500


def get_patients():
    patients = db.session.query(Patient, States, Counties).select_from(Patient).all()\

    if patients:
        result = patients_schema.dump(patients)
        return jsonify({"message": "Lista de pacientes encontrada.", "data": result})

    return jsonify({"message": "Pacientes não encontrados.", "data": {}})


def get_patient(patient_id):
    patient = Patient.query.get(patient_id)

    if patient:
        result = patient_schema.dump(patient)
        return jsonify({"message": "Paciente encontrado", "data": result}), 200

    return jsonify({"message": "Paciente não encontrado.", "data": {}}), 404


def get_patient_by_cpf(cpf):
    patient = Patient.query.filter(Patient.cpf == cpf).one()

    if patient:
        result = patient_schema.dump(patient)
        state = States.query.filter(States.id == patient.residenceUfId).one()
        result["state"] = state_schema.dump(state)
        county = Counties.query.filter(Counties.id == patient.residenceMunId).one()
        result["county"] = county_schema.dump(county)
        info_patient = InfoPatient.query.filter(InfoPatient.id_patient == patient.id).one()
        result["info_patient"] = infoPatient_schema.dump(info_patient)

        return jsonify({"message": "Paciente encontrado", "data": result}), 200

    return jsonify({"message": "Paciente não encontrado.", "data": {}}), 404


def get_result_by_cpf(cpf):
    patient = Patient.query.filter(Patient.cpf == cpf).one()

    if not patient:
        return jsonify({"message": "Paciente não encontrado.", "data": {}}), 404

    result = get_result(patient.id)
    print(result)
    if bool(result):
        return jsonify({"message": "Resultado Encontrado", "data": result}), 200
    else:
        return jsonify({"message": "Resultado não encontrado", "data": None}), 404


def delete_patient(patient_id):
    patient = Patient.query.get(patient_id)
    try:
        db.session.delete(patient)
        db.session.commit()
        result = patient_schema.dump(patient)
        return jsonify({"message": "Paciente deletado", "data": result}), 200
    except Exception as e:
        print(e)
        return jsonify({"message": "Falha para deletar paciente.", "data": {}}), 500


def get_patient_by_id(patient_id):
    patient = Patient.query.get(patient_id)

    if patient:
        result = patient_schema.dump(patient)
        return result, 200

    return None
