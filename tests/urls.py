import json
from werkzeug.security import generate_password_hash
def test_login(app, user_service, client):
    username = 'test'
    user_pass = generate_password_hash('test123')
    data = {"username": "test","password":"test123"}
    with app.app_context():
        response, code = user_service.register_user(username, user_pass)  # Assuming similar methods in AccountService
        resp = response.json
        assert "access_token" in resp
        dict_response = client.post("/api/auth/login", content_type='application/json', json=json.dumps(data)) 
        resp = dict_response.get_data(as_text=True)
        assert not isinstance(response, tuple)

    