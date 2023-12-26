from datetime import timedelta
from dotenv import dotenv_values
env = dotenv_values(".env")
class Config:
    SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://{env['USER']}:{env['PASSWORD']}@{env['HOST']}:{env['PORT']}/{env['DATABASE']}"
    SECRET_KEY= env['SECRET_KEY'] if 'SECRET_KEY' in env else 'weaksecretkey123'
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(minutes=15)  # Tempo de expiração do access_token
    JWT_REFRESH_TOKEN_EXPIRES = timedelta(days=30)  # Tempo de expiração do refresh_token

class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    TESTING = True
