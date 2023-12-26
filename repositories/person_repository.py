from pymysql import OperationalError
import pymysql
from backend.app import db
from backend.models.pessoa import Pessoa


class PersonRepository:
    @staticmethod
    def create_person(user, nome, cpf, data_nascimento):
        try:    
            new_person = Pessoa(user=user, nome=nome, cpf=cpf, data_nascimento=data_nascimento)
            db.session.add(new_person)
            db.session.commit()
            return new_person
        except:
            raise Exception("Campos inválidos") 

    @staticmethod
    def get_person_by_id(person_id):
        try:
            return Pessoa.query.get(person_id)
        except:
            raise Exception("Campos inválidos") 

    @staticmethod
    def update_person(person, **kwargs):
        try:
            for key, value in kwargs.items():
                setattr(person, key, value)
            db.session.commit()
        except:
            raise Exception("Campos inválidos") 

    @staticmethod
    def delete_person(person):
        try:
            db.session.delete(person)
            db.session.commit()
        except:
            raise Exception("Campos inválidos") 
