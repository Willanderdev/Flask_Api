from flask_restful import Resource
from api import api
from ..schemas import professor_schemas
from flask import request, make_response, jsonify
from ..entidades import professor
from ..services import professor_services
from flask_jwt_extended import jwt_required
from ..decorator import admin_required

class Professorlist(Resource):
    @jwt_required()
    def get(self):
        professores = professor_services.listarprofessores()
        ps = professor_schemas.ProfessorSchema(many=True)
        return make_response(ps.jsonify(professores), 200)

    @admin_required
    def post(self):
        ps = professor_schemas.ProfessorSchema()
        validade = ps.validate(request.json)
        if validade:
            return make_response(jsonify(validade), 400)
        else:
            nome = request.json["nome"]
            idade = request.json["idade"]

            novo_professor = professor.Formacao(nome=nome, idade=idade)
            resultado = professor_services.cadastrar_professor(novo_professor)
            x = ps.jsonify(resultado)

            return make_response(x, 201)


class ProfessorDetail(Resource):
    @admin_required
    def get(self, id):
        professor = professor_services.Listar_professor_id(id)
        if professor is None:
            return make_response(jsonify("professor nao foi encontrado"), 404)
        ps = professor_schemas.ProfessorSchema()
        return make_response(ps.jsonify(professor), 200)

    @admin_required
    def put(self, id):
        professor_bd = professor_services.Listar_professor_id(id)
        if professor_bd is None:
            return make_response(jsonify('professor nao encontrado'), 404)
        ps = professor_schemas.ProfessorSchema()
        validade = ps.validate(request.json)
        if validade:
            return make_response(jsonify(validade), 400)
        else:
            nome = request.json["nome"]
            idade = request.json["idade"]

            novo_professor = professor.Formacao(nome=nome, idade=idade)
            professor_services.atualiza_professor(professor_bd, novo_professor)
            professor_atualizado = professor_services.Listar_professor_id(id)
            return make_response(ps.jsonify(professor_atualizado), 200)

    @admin_required
    def delete(self, id):
        professor_bd = professor_services.Listar_professor_id(id)
        if professor_bd is None:
            return make_response(jsonify("professor nao encontrada"), 404)
        professor_services.remove_professor(professor_bd)
        make_response("professor excluido com sucesso", 204)


api.add_resource(Professorlist, '/professores')
api.add_resource(ProfessorDetail, '/professores/<int:id>')
