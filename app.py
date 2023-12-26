import logging
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from sqlalchemy import QueuePool
from backend.config import Config
from flask_cors import CORS

db = SQLAlchemy(engine_options={"pool_recycle":60 * 5, "pool_size": 10, "poolclass":QueuePool, "pool_pre_ping":True})
migrate = Migrate()
jwt = JWTManager()

def create_app(test_db=None):
    app = Flask(__name__)
   
    app.config.from_object(Config)
    from backend.controllers.conta_controller import account_bp
    app.register_blueprint(account_bp)
    from backend.controllers.transacao_controller import transacao_bp
    app.register_blueprint(transacao_bp)
    from backend.controllers.user_auth_controller import auth_bp
    app.register_blueprint(auth_bp)
    from backend.controllers.pessoa_controller import person_bp
    app.register_blueprint(person_bp)
    if test_db:
        app.config['SQLALCHEMY_DATABASE_URI'] = test_db
    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)
    CORS(app, resources={r"/*": {"origins": "*"}},  supports_credentials=True)
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
