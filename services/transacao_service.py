from decimal import Decimal
from backend.models.conta import Conta
from backend.models.pessoa import Pessoa
from backend.repositories.account_repository import AccountRepository
from backend.repositories.transacao_repository import TransacaoRepository
from flask import jsonify, request

class TransacaoService:
    @staticmethod
    def create_transacao(user_id,conta_destino_id, valor):
        try:
            valor = Decimal(valor)
            if valor < 1:
                raise ValueError("Valor inválido")
            conta = Conta.query.join(Pessoa).filter(Pessoa.user_id==user_id).first()
            conta_destino = Conta.query.get(conta_destino_id)
            if not conta_destino or not conta_destino_id:
                raise ValueError("Conta destino não selecionada")
            if conta.saldo >= valor and conta_destino.flag_ativo:
                TransacaoRepository.create_transacao(conta.id_conta, conta_destino,valor)
                AccountRepository.update_account(conta, saldo=(conta.saldo-valor))
                AccountRepository.update_account(conta_destino, saldo=(conta_destino.saldo+valor))
            else:
                if conta.saldo <= valor:
                    raise ValueError("Saldo insuficiente")
                else:
                    raise ValueError("Conta destino bloqueada")
            
            return jsonify({"msg": str("Transação realizada com sucesso")}), 201
        except ValueError as e:
            return jsonify({"msg": str(e)}), 201
        except Exception as e:
            return jsonify({"msg": str(e)}), 201
        
    @staticmethod
    def get_transacao_by_id(transacao_id):
        try:
            transacao = TransacaoRepository.get_transacao_by_id(transacao_id)
            return jsonify(transacao.to_dict()), 200
        except ValueError as e:
            return jsonify({"msg": str(e)}), 201
        except Exception as e:
            return jsonify({"msg": str(e)}), 201

    @staticmethod
    def get_transacao_by_user_id(user_id):
        try:
            transacao = TransacaoRepository.get_transacao_by_user_id(user_id)
            return jsonify(transacao.to_dict()), 200
        except ValueError as e:
            return jsonify({"msg": str(e)}), 201
        except Exception as e:
            return jsonify({"msg": str(e)}), 201
    
    def get_transacao_all():
        try:
            transacao = TransacaoRepository.get_transacao_all()
            return jsonify(transacao), 200
        except ValueError as e:
            return jsonify({"msg": str(e)}), 201
        except Exception as e:
            return jsonify({"msg": str(e)}), 201
                        



    @staticmethod
    def update_transacao(transacao_id, **kwargs):
        try:
            transaction = TransacaoService.get_transacao_by_id(transacao_id)
            data = request.get_json()
            id_conta = data.get('id_conta')
            valor = data.get('valor')

            if id_conta is not None:
                transaction.id_conta = id_conta
            if valor is not None:
                transaction.valor = valor
            TransacaoRepository.update_transacao(transaction, **kwargs)
            return jsonify(transaction.to_dict()), 200
        
        except ValueError as e:
            return jsonify({"msg": str(e)}), 201
        except Exception as e:
            return jsonify({"msg": str(e)}), 404
    
    @staticmethod
    def delete_transacao(transacao):
        
        try:
            transacao = TransacaoService.get_transacao_by_id(transacao)
        
            TransacaoRepository.delete_transacao(transacao)

            return jsonify({'msg': 'Transação excluída com sucesso'}), 200
       
        except ValueError as e:
            return jsonify({"msg": str(e)}), 201
        except Exception as e:
            return jsonify({"msg": str(e)}), 201
    