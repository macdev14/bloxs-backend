from flask import Blueprint, jsonify, request
from flask_cors import cross_origin
from backend.services.person_service import PersonService
from flask_jwt_extended import jwt_required, get_jwt_identity
from apiflask import APIBlueprint

person_bp = Blueprint('person', __name__, url_prefix='/api/pessoa')

@person_bp.route('/create', methods=['POST'])
@cross_origin()
@jwt_required()
def create_person():
    data = request.get_json()
    nome = data.get('nome')
    cpf = data.get('cpf')
    data_nascimento = data.get('data_nascimento')
    current_user = get_jwt_identity()

    new_person = PersonService.create_person(nome, cpf, data_nascimento, current_user)
    return jsonify(new_person.to_dict()), 201

@person_bp.route('/update/<int:person_id>', methods=['PUT'])
@cross_origin()
@jwt_required()
def update_person(person_id):
    person = PersonService.get_person_by_id(person_id)
    if not person:
        return jsonify({'error': 'Person not found'}), 404

    data = request.get_json()
    nome = data.get('nome')
    cpf = data.get('cpf')
    data_nascimento = data.get('data_nascimento')

    if nome is not None:
        person.nome = nome
    if cpf is not None:
        person.cpf = cpf
    if data_nascimento is not None:
        person.data_nascimento = data_nascimento

    PersonService.update_person(person)
    return jsonify(person.to_dict()), 200

@person_bp.route('/delete/<int:person_id>', methods=['DELETE'])
@cross_origin()
@jwt_required()
def delete_person(person_id):
    person = PersonService.get_person_by_id(person_id)
    if not person:
        return jsonify({'error': 'Person not found'}), 404

    PersonService.delete_person(person)
    return jsonify({'message': 'Person deleted successfully'}), 200


@person_bp.route('/get/<int:person_id>', methods=['GET'])
@cross_origin()
@jwt_required()
def get_person(person_id):
    person = PersonService.get_person_by_id(person_id)
    if not person:
        return jsonify({'error': 'Person not found'}), 404
    return jsonify(person.to_dict()), 200

