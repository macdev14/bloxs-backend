from backend.repositories.user_repository import UserRepository
from flask import jsonify, request
from flask_jwt_extended import create_access_token
class UserService:
    @staticmethod
    def register_user(username, password):
        try:
            user = UserRepository.create_user(username, password)
            access_token = UserRepository.generate_access_token(user.to_json()) 
            refresh_token = UserRepository.generate_refresh_token(user.to_json())   # Gera o token com a identidade do usuário
            return jsonify(access_token=access_token, refresh_token=refresh_token), 200      
        except ValueError as e:
            return jsonify({"msg": str(e)}), 201
        except Exception as e:
            return jsonify({"msg": str(e)}), 201
    @staticmethod
    def login_user(username, password):
        try:
            user = UserRepository.find_user_by_username(username)
            if user: 
                UserRepository.verify_user_password(user, password)  
                user = user.to_json()
                access_token = UserRepository.generate_access_token(user) 
                refresh_token = UserRepository.generate_refresh_token(user) 
                return jsonify(access_token=access_token, refresh_token=refresh_token), 200
            else:
                raise Exception("User not found")
        except ValueError as e:
            print(str(e))
            return jsonify({"msg": str(e)}), 201
        except Exception as e:
            print(str(e))
            return jsonify({"msg": str(e)}), 201
        
    @staticmethod
    def create_user_with_person(username, password, tipo_conta,**person_data):
        try:
            user = UserRepository.create_user_with_person(username, password, tipo_conta, **person_data)
            access_token = UserRepository.generate_access_token(user.to_json()) 
            refresh_token = UserRepository.generate_refresh_token(user.to_json())   # Gera o token com a identidade do usuário
            return jsonify(access_token=access_token, refresh_token=refresh_token), 200      
        except ValueError as e:
            return jsonify({"msg": str(e)}), 201
        except Exception as e:
            return jsonify({"msg": str(e)}), 201
        
    @staticmethod
    def get_user(username):
        try:
            user = UserRepository.find_user_by_username(username)
            return user
        except ValueError as e:
            print(str(e))
            return jsonify({"msg": str(e)}), 201
        except Exception as e:
            print(str(e))
            return jsonify({"msg": str(e)}), 201
        