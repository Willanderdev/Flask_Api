from flask_restful import Resource
from api import api
from ..schemas import usuario_schema
from flask import request, make_response, jsonify
from ..entidades import usuario
from ..services import usuario_service
import uuid


class UsuarioList(Resource):

    def post(self):
        us = usuario_schema.UsuarioSchema()
        validade = us.validate(request.json)
        if validade:
            return make_response(jsonify(validade), 400)
        else:
            nome = request.json["nome"]
            email = request.json["email"]
            senha = request.json["senha"]
            is_admin = request.json["is_admin"]
            api_key = str(uuid.uuid4())

            novo_usuario = usuario.Usuario(nome=nome, email=email, senha=senha, is_admin=is_admin, api_key=api_key)
            resultado = usuario_service.cadastrar_usuario(novo_usuario)
            x = us.jsonify(resultado)
            return make_response(x, 201)


api.add_resource(UsuarioList, '/usuario')

