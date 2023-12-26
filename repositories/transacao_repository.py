from datetime import datetime, timezone, tzinfo

from sqlalchemy import extract, func
from backend.app import db
from backend.models.transacao import Transacao

class TransacaoRepository:
    @staticmethod
    def create_transacao(id_conta, conta_destino, valor):
        try:
            new_transaction = Transacao(conta=id_conta, conta_destino=conta_destino, valor=valor)
            db.session.add(new_transaction)
            db.session.commit()
            return new_transaction
        except Exception as e:
            raise Exception(str(e)) 


    @staticmethod
    def get_transacao_by_id(transaction_id):
        try:
            return Transacao.query.get(transaction_id)
        except Exception as e:
            raise Exception("Não foi possível encontrar a transação") 

    @staticmethod
    def get_transacao_all():
        try:
            return [i.to_dict() for i in Transacao.query.all()]
        except Exception as e:

            raise Exception(str(e)) 

    @staticmethod
    def get_transacao_by_user_id(user_id):
        try:
            return Transacao.query.filter(user_id=user_id)
        except Exception as e:
            raise Exception("Não foi possível encontrar transação deste usuário") 

    @staticmethod
    def update_transacao(transacao, **kwargs):
        try:
            for key, value in kwargs.items():
                setattr(transacao, key, value)
            db.session.commit()
        except Exception as e:
            raise Exception("Não foi possível atualizar transação") 
        
    @staticmethod
    def delete_transacao(transacao):
        try:
            db.session.delete(transacao)
            db.session.commit()
        except Exception as e:
            raise Exception("Não foi possível excluir transação") 

    @staticmethod
    def get_transacao_valor_total_diario(id):
        try:
           

            current_date = datetime.now(timezone.utc).date()
            qry = (
                        Transacao.query
                        .with_entities(func.sum(Transacao.valor))
                        .filter(
                            Transacao.id_conta == id,
                            Transacao.id_conta_destino == id,
                            extract('year', Transacao.data_transacao) == current_date.year,
                            extract('month', Transacao.data_transacao) == current_date.month,
                            extract('day', Transacao.data_transacao) == current_date.day
                        )
                        .group_by(Transacao.id_conta)
                        .scalar()
                    )
            total = qry if qry else 0
            return total
        except Exception as e:

            raise Exception(str(e)) 