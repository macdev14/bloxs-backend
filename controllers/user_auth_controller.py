from datetime import timedelta, timezone
import datetime
import json
from flask_cors import cross_origin
from backend import app
from backend.models.schemas import UserSchema
from flask import Blueprint, jsonify, request
from backend.services.user_service import UserService
from flask_jwt_extended import create_access_token, get_jwt, get_jwt_identity, jwt_required, set_access_cookies
from apiflask import APIBlueprint
auth_bp = Blueprint('auth', __name__, url_prefix='/api/auth')

@auth_bp.route('/cadastro', methods=['POST'])
@cross_origin()
def register():
    data = request.json
    username = data.get('username')
    password = data.get('password')
    pessoa = data.get('person')
    tipo_conta=data.get('tipo_conta')
    return UserService.create_user_with_person(username, password, tipo_conta, **pessoa)
        

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.json
    if isinstance(data, str):
        data = json.loads(data)
    username = data.get('username')
    password = data.get('password')
    return UserService.login_user(username, password)

@auth_bp.route("/refresh", methods=["POST"])
@jwt_required(refresh=True)
def refresh():
    identity = get_jwt_identity()
    access_token = create_access_token(identity=identity)
 
    return jsonify(access_token=access_token)


