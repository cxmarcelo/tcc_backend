from app import app
from flask import jsonify
from ..views import users, helper, counties, states, occupation, patient, info_patient


@app.route("/", methods=['GET'])
def root():
    return jsonify({'message': "API Started"})


@app.route("/users", methods=['POST'])
def post_user():
    return users.post_user()


@app.route("/users/<user_id>", methods=['PUT'])
def update_user(user_id):
    return users.update_user(user_id)


@app.route("/users", methods=['GET'])
def get_users():
    return users.counties_by_ufId()


@app.route("/users/<user_id>", methods=['GET'])
@helper.token_required
def get_user(current_user, user_id):
    return users.get_user(user_id)


@app.route("/users/<user_id>", methods=['DELETE'])
def delete_user(user_id):
    return users.delete_user(user_id)


@app.route("/auth", methods=['POST'])
def authenticate():
    return helper.auth()


@app.route("/municipios", methods=['GET'])
def get_all_counties():
    return counties.get_counties()


@app.route("/municipios/<uf_id>", methods=['GET'])
def get_counties(uf_id):
    return counties.counties_by_ufId(uf_id)


@app.route("/states", methods=['GET'])
def get_states():
    return states.get_states()


@app.route("/states/<uf_id>", methods=['GET'])
def get_state(uf_id):
    return states.get_state_by_id(uf_id)


@app.route("/occupations", methods=['GET'])
def get_occupations():
    return occupation.get_occupations()


@app.route("/occupations/<occupation_id>", methods=['GET'])
def get_occupation_by_id(occupation_id):
    return occupation.get_occupation_by_id(occupation_id)


@app.route("/patient", methods=['POST'])
def insert_patient():
    return patient.post_patient()


@app.route("/patient", methods=['GET'])
def get_patients():
    return patient.get_patients()


@app.route("/patient/<patient_id>", methods=['GET'])
def get_patient(patient_id):
    return patient.get_patient(patient_id)


@app.route("/search_patient_cpf/<cpf>", methods=['GET'])
def get_patient(cpf):
    return patient.get_patient_by_cpf(cpf)


@app.route("/info_patient", methods=['POST'])
def insert_patient():
    return info_patient.post_infoPatient()
