from flask import jsonify
from pymysql import OperationalError
from backend.app import db
from backend.models.usuario import Usuario
from backend.models.pessoa import Pessoa
from backend.repositories.account_repository import AccountRepository
from backend.repositories.person_repository import PersonRepository
from werkzeug.security import check_password_hash, generate_password_hash
from flask_jwt_extended import create_access_token, create_refresh_token

class UserRepository:
    @staticmethod
    def create_user_with_person(username, password, tipo_conta, **person_data):
        try:
            existing_user = Usuario.query.filter_by(username=username).first()
            if existing_user:
                raise ValueError("O nome de usuário já está em uso")
            new_user = UserRepository.create_user(username=username, password=password)
            new_person = PersonRepository.create_person(user=new_user, **person_data)
            AccountRepository.create_account(new_person, tipo_conta)
           
            return new_user
        except OperationalError as e:
            raise Exception("Campos inválidos") 

    @staticmethod
    def create_user(username, password):
        try:
            existing_user = Usuario.query.filter_by(username=username).first()
            if existing_user:
                raise ValueError("O nome de usuário já está em uso")
            hashed_password = generate_password_hash(password)
            new_user = Usuario(username=username, password=hashed_password)
            db.session.add(new_user)
            db.session.commit()
            return new_user
        except OperationalError as e:
            raise Exception("Campos inválidos")
    @staticmethod
    def find_user_by_username(username):
        user = Usuario.query.filter_by(username=username).first()
        if not user:
            return None
        return user
            
    @staticmethod
    def verify_user_password(user, password):
        valido  = check_password_hash(user.password, password)
        if not valido:
            raise Exception("Credenciais Inválidas")
        return valido
    @staticmethod
    def generate_access_token(username):
        access_token = create_access_token(identity=username)
        return access_token
    
    @staticmethod
    def generate_refresh_token(username):
        refresh_token = create_refresh_token(identity=username)
        return refresh_token