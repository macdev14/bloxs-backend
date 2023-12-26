import json
from flask import request, Blueprint
from flask_cors import cross_origin
from flask_jwt_extended import get_jwt_identity, jwt_required
from backend.services.transacao_service import TransacaoService


transacao_bp = Blueprint('transacao', __name__, url_prefix='/api/transacao')

@transacao_bp.route('/get/<int:transacao_id>', methods=['GET'])
@jwt_required()
def get_transaction(transacao_id):
    return TransacaoService.get_transacao_by_id(transacao_id)

@transacao_bp.route('/get/user', methods=['GET'])
@jwt_required()
def get_user_transaction():
    current_user = get_jwt_identity()
    return TransacaoService.get_transacao_by_user_id(current_user.id)

@transacao_bp.route('/get/all', methods=['GET'])
@jwt_required()
def get_all_transactions():
    return TransacaoService.get_transacao_all()

@transacao_bp.route('/create', methods=['POST'])
@jwt_required()
def criar_transacao():
    data = request.get_json()
    valor = data.get('valor')
    conta_destino_id = data.get('id_conta_destino')
    current_user = json.loads(get_jwt_identity())
    return TransacaoService.create_transacao(current_user['id'],conta_destino_id, valor)
       
@transacao_bp.route('/update/<int:transacao_id>', methods=['PUT'])
@jwt_required()
def atualizar_transacao(transacao_id):
    return TransacaoService.update_transacao(transacao_id)
        
@transacao_bp.route('/delete/<int:transacao_id>', methods=['DELETE'])
@jwt_required()
def excluir_transacao(transacao_id):
    return TransacaoService.delete_transacao(transacao_id)
    
    




