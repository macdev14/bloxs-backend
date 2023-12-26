from decimal import Decimal
from flask import jsonify
from backend.models.usuario import Usuario
from backend.repositories.account_repository import AccountRepository
from backend.repositories.transacao_repository import TransacaoRepository

class AccountService:
    @staticmethod
    def create_account(id_pessoa, tipo_conta):
        try:
            return AccountRepository.create_account(id_pessoa, tipo_conta)
        except ValueError as e:
            return jsonify({"msg": str(e)}), 201
        except Exception as e:
            return jsonify({"msg": str(e)}), 201
    @staticmethod
    def get_account_by_id(account_id):
        try:
            return AccountRepository.get_account_by_id(account_id)
        except ValueError as e:
            return jsonify({"msg": str(e)}), 201
        except Exception as e:
            return jsonify({"msg": str(e)}), 201
        
    @staticmethod
    def get_account_by_user_id(user_id):
        try:
            return AccountRepository.get_account_by_user_id(user_id)
        except ValueError as e:
            return jsonify({"msg": str(e)}), 201
        except Exception as e:
            return jsonify({"msg": str(e)}), 201
            

    def get_saldo_by_id(account_id):
        try:
            conta = AccountRepository.get_account_by_id(account_id)
            return conta.saldo
        except ValueError as e:
            return jsonify({"msg": str(e)}), 201
        except Exception as e:
            return jsonify({"msg": str(e)}), 201
        
    def realizar_saque(user_id, valor):
        try:
            valor = Decimal(valor.replace(',','.'))
            valid = valor > 0.01
            if not valid: raise ValueError()
            conta = AccountRepository.get_account_by_user_id(user_id)
            tem_saldo_suficiente = conta.saldo >= valor

            limite_diario  = TransacaoRepository.get_transacao_valor_total_diario(conta.id_conta)
            tem_limite = conta.limite_saque_diario > limite_diario
            valor_limite_diario = conta.limite_saque_diario >= valor

            if tem_saldo_suficiente and tem_limite and valor_limite_diario:
                TransacaoRepository.create_transacao(conta,conta,valor)
                AccountRepository.update_account(conta, saldo=(conta.saldo-valor))
                return jsonify({"msg": "Saque de R$"+ str(valor) +" realizado" }), 201
            elif not tem_saldo_suficiente: 
                return jsonify({"msg": "Saldo Insuficiente" }), 201
            elif not tem_limite: 
                return jsonify({"msg": "Limite de saque diário excedido" }), 201
            elif not valor_limite_diario: 
                return jsonify({"msg": "Valor excede limite de saque diário " }), 201
        except ValueError as e:
            return jsonify({"msg": str("Valor inválido")}), 201
        except Exception as e:
            return jsonify({"msg": str("Valor inválido")}), 201

    def realizar_deposito(user_id, valor):
        try:
            valor = Decimal(valor.replace(',','.'))
            valid = valor > 0.01
            if not valid: raise ValueError()
            conta = AccountRepository.get_account_by_user_id(user_id)
            AccountRepository.update_account(conta, saldo=(conta.saldo+valor))
            return jsonify({"msg": "Deposito de R$"+ str(valor) +" realizado" }), 201
        except ValueError as e:
            return jsonify({"msg": str("Valor inválido")}), 201
        except Exception as e:
            return jsonify({"msg": str("Valor inválido")}), 201

    @staticmethod
    def get_all_accounts(curr):
        try:
            return AccountRepository.get_all_accounts_except_user(int(curr))
        except ValueError as e:
            return jsonify({"msg": str(e)}), 201
        except Exception as e:
            return jsonify({"msg": str(e)}), 201

    

    @staticmethod
    def update_account(account, **kwargs):
        try:
            print('kwargs before')
            print(kwargs)
            if 'pessoa' in kwargs:
                kwargs.pop('pessoa')
            kwargs.pop('id_conta')
            print('kwargs after')
            print(kwargs)
            return AccountRepository.update_account(account, **kwargs)
        except ValueError as e:
            return jsonify({"msg": str(e)}), 201
        except Exception as e:
            return jsonify({"msg": str(e)}), 201

    
    @staticmethod
    def deactivate_account(account, **kwargs):
        try:
            account = AccountRepository.get_account_by_id(account).to_dict()
            account.flag_ativo = False
            return AccountRepository.update_account(account, **kwargs)
        except ValueError as e:
            return jsonify({"msg": str(e)}), 201
        except Exception as e:
            return jsonify({"msg": str(e)}), 201

    @staticmethod
    def activate_account(account, **kwargs):
        try:
            account = AccountRepository.get_account_by_id(account).to_dict()
            account.flag_ativo = True
            return AccountRepository.update_account(account, **kwargs)
        except ValueError as e:
            return jsonify({"msg": str(e)}), 201
        except Exception as e:
            return jsonify({"msg": str(e)}), 201


    @staticmethod
    def delete_account(account):
        try:
            return AccountRepository.delete_account(account)
        except ValueError as e:
            return jsonify({"msg": str(e)}), 201
        except Exception as e:
            return jsonify({"msg": str(e)}), 201