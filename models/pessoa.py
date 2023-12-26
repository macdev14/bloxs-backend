import json
from backend.app import db
from datetime import datetime

from backend.models.usuario import Usuario

class Pessoa(db.Model):
    __tablename__ = 'pessoa'

    id_pessoa = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    cpf = db.Column(db.String(14), unique=True, nullable=False)
    data_nascimento = db.Column(db.Date, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('usuario.id', ondelete='CASCADE'), unique=True, nullable=False)
    user = db.relationship('Usuario', backref='person', uselist=False)

    def __init__(self, user, nome, cpf, data_nascimento):
        self.nome = nome
        self.cpf = cpf
        self.data_nascimento = data_nascimento
        is_user_id = isinstance(user, int)
        if is_user_id:
            user = Usuario.query.get(user)
        if user:
            self.user = user
            self.user_id = user.id

    def to_dict(self):
        return {
            'id_pessoa': self.id_pessoa,
            'nome': self.nome,
            'cpf': self.cpf,
            'data_nascimento': self.data_nascimento.strftime('%Y-%m-%d')
        }
    
    def to_json(self):
        return json.dumps(self.to_dict())
