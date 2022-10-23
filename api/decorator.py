from functools import wraps
from flask_jwt_extended import get_jwt, verify_jwt_in_request
from flask import make_response, jsonify, request
from .services.usuario_service import listar_usuario_api_key


#implementar o decorator pra vericar se o login tem autenticação do token e autorização "admin" pra fazer modificações no arquivo
def admin_required(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        verify_jwt_in_request()
        claims = get_jwt()
        if claims["roles"] != 'admin':
            return make_response(jsonify(mensagem='somente o admin tem autorização pra alterar dados'), 403)
        else:
            return fn(*args, **kwargs)

    return wrapper


def api_key_required(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        api_key = request.args.get('api_key')
        if api_key and listar_usuario_api_key(api_key):
            return fn(*args, **kwargs)
        else:
            return make_response(jsonify(mensagem='API_KEY INVALIDA'), 401)

    return wrapper
