

def validate(user_dict):
    name = user_dict['name']
    auth_token = user_dict['auth_token']
    auth_token_secret = user_dict['auth_token_secret']
    user_id = user_dict['user_id']
    if len(name) == 0 and len(auth_token) == 0 and len(auth_token_secret) == 0 and len(user_id) == 0:
        raise ValueError("Usuario Invalido")
