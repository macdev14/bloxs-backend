

import json
from flask_cors import cross_origin
from flask_jwt_extended import get_jwt_identity, jwt_required
from backend.models.schemas import ContaSchema
from backend.services.account_service import AccountService
from flask import Blueprint, jsonify, make_response, request

account_bp = Blueprint('conta', __name__, url_prefix='/api/conta')

@account_bp.route('/create', methods=['POST'])
@jwt_required()
def create_account():
    data = request.get_json()
    id_pessoa = data.get('id_pessoa')
    tipo_conta = data.get('tipo_conta')
    new_account = AccountService.create_account(id_pessoa, tipo_conta)
    return jsonify(new_account.to_dict()), 201

@account_bp.route('/update', methods=['PUT'])
@jwt_required()
def update_account():
    current_user = json.loads(get_jwt_identity())
    account = AccountService.get_account_by_user_id(current_user['id'])
    if not account:
        return jsonify({'error': 'Account not found'}), 404

    data = request.get_json()
    print('flag: ', data.get('flag_ativo'))
    AccountService.update_account(account, **data)
    return jsonify(account.to_dict()), 201

@account_bp.route('/update/saque', methods=['PUT'])
@jwt_required()
def saque_account():
    current_user = json.loads(get_jwt_identity())
    data = request.get_json()
    valor = data.get('valor')
    return AccountService.realizar_saque(current_user['id'], valor)


@account_bp.route('/update/deposito', methods=['PUT'])
@jwt_required()
def deposito_account():
    current_user = json.loads(get_jwt_identity())
    data = request.get_json()
    valor = data.get('valor')
    return AccountService.realizar_deposito(current_user['id'], valor)

@account_bp.route('/delete/<int:account_id>', methods=['DELETE'])
@jwt_required()
def delete_account(account_id):
    account = AccountService.get_account_by_id(account_id)
    if not account:
        return jsonify({'error': 'Account not found'}), 404

    AccountService.delete_account(account)
    return jsonify({'msg': 'Conta excluida com sucesso'}), 200

@account_bp.route('/get/saldo/<int:account_id>', methods=['GET'])
@jwt_required()
def get_consultar_saldo(account_id):
    account = AccountService.get_saldo_by_id(account_id)
    return jsonify(account.to_dict()), 200

@account_bp.route('/get/current', methods=['GET'])
@jwt_required()
def get_user_account():
    current_user = json.loads(get_jwt_identity())
    print(current_user)
    account = AccountService.get_account_by_user_id(current_user['id'])
    if not account:
        return jsonify({'error': 'Account not found'}), 404
    return jsonify(account.to_dict()), 200
 
@account_bp.route('/get/<int:account_id>', methods=['GET'])
@jwt_required()
def get_account(account_id=None):
    jwt_identity=json.loads(get_jwt_identity())
    if not account_id: account_id = jwt_identity['id']
    account = AccountService.get_account_by_id(account_id)
    if not account:
        return jsonify({'error': 'Account not found'}), 404
    return jsonify(account.to_dict()), 200

@account_bp.route('/get/all', methods=['GET'])
@jwt_required()
def get_all_accounts():
    current_user = json.loads(get_jwt_identity())
    accounts = AccountService.get_all_accounts(curr=current_user['id'])
    
    if not accounts:
        return jsonify({'error': 'Não há contas'}), 404
    return make_response(accounts), 200

