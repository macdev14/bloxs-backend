from flask import jsonify
from backend.app import db
from backend.models.conta import Conta
from backend.models.pessoa import Pessoa
class AccountRepository:


    @staticmethod
    def create_account(pessoa, tipo_conta):
        
        new_account = Conta(pessoa=pessoa, tipo_conta=tipo_conta)
        db.session.add(new_account)
        db.session.commit()
        return new_account

    @staticmethod
    def get_account_by_id(account_id):
        return Conta.query.get(account_id)


    
    @staticmethod
    def get_all_accounts_except_user(curr_user_id):
        # Assuming 'curr_user' is an instance of the 'Person' model
        contas = [i.to_dict() for i in Conta.query.join(Pessoa).filter(Pessoa.user_id != curr_user_id).all()]
       
        return contas

    @staticmethod
    def update_account(account, **kwargs):
        
        for key, value in kwargs.items():
            if key!='id_conta':
                setattr(account, key, value)
        db.session.commit()

    @staticmethod
    def delete_account(account):
        db.session.delete(account)
        db.session.commit()

    @staticmethod
    def get_account_by_user_id(user_id):
        conta = Conta.query.join(Pessoa).filter(Pessoa.user_id == user_id).first()
        return conta
    