import json
from backend.app import db
from werkzeug.security import generate_password_hash, check_password_hash

class Usuario(db.Model):
    __tablename__ = 'usuario'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    def __init__(self, username, password):
        self.username = username
        self.password = generate_password_hash(password)  # Gera um hash da senha para armazenar no banco de dados
       
    def check_password(self, password):
        return check_password_hash(self.password, password)  # Verifica se a senha fornecida corresponde ao hash no banco de dados

    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username
        }
    
    def to_json(self):
        return json.dumps(self.to_dict())
