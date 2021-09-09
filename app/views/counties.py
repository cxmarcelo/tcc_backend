from app import db
from flask import request, jsonify
from ..models.counties import Counties, county_schema, counties_schema


def post_county():
    county_id = request.json['id']
    name = request.json['name']
    uf_id = request.json['uf_id']
    county = Counties(county_id, name, uf_id)

    try:
        db.session.add(county)
        db.session.commit()
        result = county_schema.dump(county)
        return jsonify({'message': 'Município Inserido', 'data': result}), 201
    except Exception as e:
        print(e)
        return jsonify({'message': 'Erro para inserir município', 'data': {}}), 500


def get_county(county_id):
    county = Counties.query.get(county_id)

    if county:
        result = county_schema.dump(county)
        return jsonify({"message": "Município eoncontrado.", "data": result}), 200

    return jsonify({"message": "Município não encontrado.", "data": {}}), 404


def get_counties():
    name = request.args.get('name')
    if not name:
        name = ""
    counties = Counties.query.filter(Counties.name.like(f'{name}%'))

    if counties:
        result = counties_schema.dump(counties)
        return jsonify({"message": "Municípios encontrados", "data": result}), 200

    return jsonify({"message": "Nenhum Município encontrado", "data": {}}), 200


def counties_by_ufId(uf_id):
    name = request.args.get('name')
    if not name:
        name = ""

    counties = Counties.query.filter(Counties.uf_id == uf_id).filter(Counties.name.like(f'{name}%'))

    if counties:
        result = counties_schema.dump(counties)
        return jsonify({"message": "success fetched", "data": result})

    return jsonify({"message": "nothing found", "data": {}})


"""
def delete_user(user_id):
    user = Counties.query.get(user_id)
    try:
        db.session.delete(user)
        db.session.commit()
        result = county_schema.dump(user)
        return jsonify({"message": "successfully deleted", "data": result}), 200
    except Exception as e:
        print(e)
        return jsonify({"message": "unable to delete", "data": {}}), 500
"""

