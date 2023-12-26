
from backend.repositories.person_repository import PersonRepository


class PersonService:
    @staticmethod
    def create_person(user, nome, cpf, data_nascimento):
        return PersonRepository.create_person(user, nome, cpf, data_nascimento)

    @staticmethod
    def get_person_by_id(person_id):
        return PersonRepository.get_person_by_id(person_id)

    @staticmethod
    def update_person(person, **kwargs):
        return PersonRepository.update_person(person, **kwargs)

    @staticmethod
    def delete_person(person):
        return PersonRepository.delete_person(person)
