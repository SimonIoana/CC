import jwt
import requests
import hashlib
import json

def get_user_for_mail(email):
    res = requests.get('https://tema3-cloud-309417.oa.r.appspot.com/api/v1/user?email=' + email)

    return res.json()

def check_auth_data(email, password, resp):
    if resp['data']["email"] != email or resp['data']["password"] != hashlib.md5(password.encode('UTF-8')).hexdigest():
        return False

    return True


def hello_world(request):
    request_json = request.get_json()

    if request_json and 'email' in request_json and 'password' in request_json:
        email = request_json['email']
        password = request_json['password']

        resp = get_user_for_mail(email)
        if not check_auth_data(email, password, resp):
            result = {
                "status": "error",
                "message": "Unauthorized"
            }

            return json.dumps(result), 401

        result = {
            "status": "success",
            "data": {"email": email, "id": resp['data']["id"]}
        }
        
        return json.dumps(result), 200

    else:
        return f'Bad request' + json.dumps(request_json) , 400
