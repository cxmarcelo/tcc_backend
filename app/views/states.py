from app import db
from flask import request, jsonify
from ..models.states import States, state_schema, states_schema


def post_state():
    name = request.json['name']
    initial = request.json['initial']
    state = States(name, initial)

    try:
        db.session.add(state)
        db.session.commit()
        result = state_schema.dump(state)
        return jsonify({'message': 'successfully registered', 'data': result}), 201
    except Exception as e:
        print(e)
        return jsonify({'message': 'unable to create', 'data': {}}), 500


def get_states():
    states = States.query.all()

    if states:
        result = states_schema.dump(states)
        return jsonify({"message": "success fetched", "data": result})

    return jsonify({"message": "nothing found", "data": {}})


def get_state_by_id(state_id):
    state = States.query.get(state_id)

    if state:
        result = state_schema.dump(state)
        return jsonify({"message": "Estado encontrado", "data": result}), 200

    return jsonify({"message": "Estado não encontrado.", "data": {}}), 404


def delete_user(state_id):
    state = States.query.get(state_id)
    try:
        db.session.delete(state)
        db.session.commit()
        result = state_schema.dump(state)
        return jsonify({"message": "successfully deleted", "data": result}), 200
    except Exception as e:
        print(e)
        return jsonify({"message": "unable to delete", "data": {}}), 500


def state_by_uf(uf):
    try:
        return States.query.filter(States.initials == uf).one()
    except Exception as e:
        print(e)
        return None