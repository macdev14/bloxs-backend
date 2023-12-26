import json
from datetime import datetime
from backend.app import db
from backend.models.pessoa import Pessoa
class Conta(db.Model):
    __tablename__ = 'conta'

    id_conta = db.Column(db.Integer, primary_key=True)
    id_pessoa = db.Column(db.Integer, db.ForeignKey('pessoa.id_pessoa'), nullable=False)
    pessoa = db.relationship('Pessoa', backref='conta')
    saldo = db.Column(db.Numeric(precision=10, scale=2), nullable=False, default=0.00)
    limite_saque_diario = db.Column(db.Numeric(precision=10, scale=2), nullable=False, default=1000.00)
    flag_ativo = db.Column(db.Boolean, nullable=False, default=True)
    tipo_conta = db.Column(db.Integer, nullable=False)
    data_criacao = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __init__(self, pessoa, tipo_conta):
        is_pessoa_id = isinstance(pessoa, int)
        if is_pessoa_id:
            pessoa = Pessoa.query.get(pessoa) 
        if pessoa:
            self.pessoa = pessoa
            self.id_pessoa = pessoa.id_pessoa
        self.tipo_conta = tipo_conta

    def to_dict(self):
        return {
            'id_conta': self.id_conta,
            'id_pessoa': self.id_pessoa,
            'pessoa': self.pessoa.to_dict() if self.pessoa else Pessoa.query.get(self.id_pessoa).to_dict(),
            'saldo': float(self.saldo),
            'limite_saque_diario': float(self.limite_saque_diario),
            'flag_ativo': self.flag_ativo,
            'tipo_conta': self.tipo_conta,
            'data_criacao':  self.data_criacao if isinstance(self.data_criacao,str) else self.data_criacao.strftime('%Y-%m-%d %H:%M:%S')
        }


    def to_json(self):
        return json.dumps(self.to_dict())
