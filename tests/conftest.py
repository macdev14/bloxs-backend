from datetime import date
from unittest.mock import MagicMock
from backend.app import create_app, db
from backend.repositories.account_repository import AccountRepository
from backend.repositories.person_repository import PersonRepository
from backend.repositories.transacao_repository import TransacaoRepository
from backend.repositories.user_repository import UserRepository
from backend.services.account_service import AccountService
from backend.services.person_service import PersonService
from backend.services.transacao_service import TransacaoService
from sqlalchemy.exc import SQLAlchemyError
import pytest
from werkzeug.security import generate_password_hash
from backend.services.user_service import UserService

@pytest.fixture(scope='module')
def app():
    app = create_app(test_db="sqlite://")
    transaction_data = {'id_conta': 1, 'valor': 100.0}
    person_data = {
        'nome': 'Exemplo Pessoa',
        'cpf': '123.456.789-00',
        'data_nascimento': date(2002, 10, 11)
    }
    created_user_pass = generate_password_hash('joao123')
    with app.app_context():
        db.create_all()
        created_user = UserRepository.create_user(username='teste', password=created_user_pass)
        created_person = PersonRepository.create_person(user=created_user, **person_data)
        created_account = AccountRepository.create_account(created_person, 1)
        transaction = TransacaoRepository.create_transacao(**transaction_data)
        
    yield app

@pytest.fixture(scope='module')
def client(app):
    return app.test_client()

@pytest.fixture(scope='module')
def account_repository():
    return AccountRepository()

@pytest.fixture(scope='module')
def person_repository():
    return PersonRepository()

@pytest.fixture(scope='module')
def transacao_repository():
    return TransacaoRepository()
@pytest.fixture(scope='module')
def user_repository():
    return UserRepository()