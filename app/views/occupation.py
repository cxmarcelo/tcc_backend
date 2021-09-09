from app import db
from flask import request, jsonify
from ..models.occupation import Occupation, occupation_schema, occupations_schema


def post_state():
    name = request.json['name']
    initial = request.json['initial']
    state = Occupation(name, initial)

    try:
        db.session.add(state)
        db.session.commit()
        result = occupation_schema.dump(state)
        return jsonify({'message': 'successfully registered', 'data': result}), 201
    except Exception as e:
        print(e)
        return jsonify({'message': 'unable to create', 'data': {}}), 500


def get_occupations():
    name = request.args.get('name')
    if not name:
        name = ""

    states = Occupation.query.filter(Occupation.name.like(f'{name}%'))

    if states:
        result = occupations_schema.dump(states)
        return jsonify({"message": "Ocupações encontradas", "data": result}), 200

    return jsonify({"message": "Nenhuma ocupação encontrada", "data": {}}), 404


def get_occupation_by_id(occupation_id):
    state = Occupation.query.get(occupation_id)

    if state:
        result = occupation_schema.dump(state)
        return jsonify({"message": "Ocupação encontrada", "data": result}), 200

    return jsonify({"message": "Ocupação não encontrada.", "data": {}}), 404
