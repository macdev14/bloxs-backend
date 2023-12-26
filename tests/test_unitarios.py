import pytest
from datetime import date
from werkzeug.security import generate_password_hash


def test_created_user(user_repository, app):
    with app.app_context():
        
        user = user_repository.find_user_by_username('teste')
        assert user is not None 


def test_created_person(person_repository, app):

    with app.app_context():
        created_person = person_repository.get_person_by_id(1)
        assert created_person is not None

def test_created_transaction(transacao_repository, app):
    with app.app_context():
        transaction = transacao_repository.get_transacao_by_id(1)
        assert transaction is not None

def test_created_account(account_repository, app):
    with app.app_context():
        account = account_repository.get_account_by_id(1)
        assert account is not None

