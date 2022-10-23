from flask_restful import Resource
from api import api
from ..schemas import formacao_schemas
from flask import request, make_response, jsonify
from ..entidades import formacao
from ..services import formacao_services
from flask_jwt_extended import jwt_required
from ..decorator import admin_required, api_key_required

class Formacaolist(Resource):
    @api_key_required
    def get(self):
        formacoes = formacao_services.listarformacao()
        cs = formacao_schemas.FormacaoSchema(many=True)
        return make_response(cs.jsonify(formacoes), 200)

    @api_key_required
    def post(self):
        cs = formacao_schemas.FormacaoSchema()
        validade = cs.validate(request.json)
        if validade:
            return make_response(jsonify(validade), 400)
        else:
            nome = request.json["nome"]
            descricao = request.json["descricao"]
            professores = request.json["professores"]
            nova_formacao = formacao.Formacao(nome=nome, descricao=descricao, professores=professores)
            resultado = formacao_services.cadastrar_formacao(nova_formacao)
            x = cs.jsonify(resultado)

            return make_response(x, 201)


class FormacaoDetail(Resource):
    @api_key_required
    def get(self, id):
        formacao = formacao_services.listar_formacao_id(id)
        if formacao is None:
            return make_response(jsonify("formacao nao foi encontrada"), 404)
        cs = formacao_schemas.FormacaoSchema()
        return make_response(cs.jsonify(formacao), 200)

    @api_key_required
    def put(self, id):
        formacao_bd = formacao_services.listar_formacao_id(id)
        if formacao_bd is None:
            return make_response(jsonify('formacao nao encontrado'), 404)
        cs = formacao_schemas.FormacaoSchema()
        validade = cs.validate(request.json)
        if validade:
            return make_response(jsonify(validade), 400)
        else:
            nome = request.json["nome"]
            descricao = request.json["descricao"]
            professores = request.json["professores"]
            nova_formacao = formacao.Formacao(nome=nome, descricao=descricao, professores=professores)
            formacao_services.atualiza_formacao(formacao_bd, nova_formacao)
            formacao_atualizado = formacao_services.listar_formacao_id(id)
            return make_response(cs.jsonify(formacao_atualizado), 200)

    @api_key_required
    def delete(self, id):
        formacao_bd = formacao_services.listar_formacao_id(id)
        if formacao_bd is None:
            return make_response(jsonify("formacao nao encontrada"), 404)
        formacao_services.remove_formacao(formacao_bd)
        make_response("formacao excluido com sucesso", 204)


api.add_resource(Formacaolist, '/formacoes')
api.add_resource(FormacaoDetail, '/formacoes/<int:id>')
