import json
from backend.app import db
from datetime import datetime

from backend.models.conta import Conta


class Transacao(db.Model):
    __tablename__ = 'transacao'

    id_transacao = db.Column(db.Integer, primary_key=True)
    
    id_conta = db.Column(db.Integer, db.ForeignKey('conta.id_conta', ondelete='CASCADE'), nullable=False)
    id_conta_destino = db.Column(db.Integer, db.ForeignKey('conta.id_conta', ondelete='CASCADE'), nullable=False)
    
    conta_destino = db.relationship('Conta', backref='transacao_destino', foreign_keys=[id_conta_destino])
    conta = db.relationship('Conta', backref='transacao', foreign_keys=[id_conta])
    
    valor = db.Column(db.Numeric(precision=10, scale=2), nullable=False)
    data_transacao = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __init__(self, conta, conta_destino, valor):
        self.valor = valor
        if not isinstance(conta, Conta):
            self.id_conta = conta
            self.conta = Conta.query.get(conta)
        else:
            self.id_conta = conta.id_conta
            self.conta = conta
        if not isinstance(conta_destino, Conta):
            self.conta_destino = Conta.query.get(conta_destino)
            self.id_conta_destino = conta_destino
        else:
            self.conta_destino = conta_destino
            self.id_conta_destino = conta_destino.id_conta
       
    def to_dict(self):
        return {
            'id_transacao': self.id_transacao,
            # 'id_conta': self.id_conta,
            'conta': self.conta.to_dict() if self.conta else Conta.query.get(self.id_conta).to_dict(),
            # 'conta_destino': self.conta_destino.to_dict() if self.conta_destino else Conta.query.get(self.id_conta_destino).to_dict(),
            'valor': float(self.valor),
            'data_transacao': self.data_transacao.strftime('%Y-%m-%d %H:%M:%S')
        }
    
    def to_json(self):
        return json.dumps(self.to_dict())
