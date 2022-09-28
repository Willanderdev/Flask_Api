from flask_restful import Resource
from api import api
from ..schemas import curso_schemas
from flask import request, make_response, jsonify
from ..entidades import curso
from ..services import curso_service, formacao_services


class Cursolist(Resource):
    def get(self):
        cursos = curso_service.listarcursos()
        cs = curso_schemas.CursoSchema(many=True)
        return make_response(cs.jsonify(cursos), 200)

    def post(self):
        cs = curso_schemas.CursoSchema()
        validade = cs.validate(request.json)
        if validade:
            return make_response(jsonify(validade), 400)
        else:
            nome = request.json["nome"]
            descricao = request.json["descricao"]
            data_publicacao = request.json["data_publicacao"]
            formacao = request.json["formacao"]
            formacao_curso = formacao_services.listar_formacao_id(formacao)
            if formacao_curso is None:
                return make_response(jsonify("formacao nao foi encontrada"), 404)
            novo_curso = curso.Curso(nome=nome, descricao=descricao, data_publicacao=data_publicacao, formacao=formacao_curso)
            resultado = curso_service.cadastrar_curso(novo_curso)
            x = cs.jsonify(resultado)

            return make_response(x, 201)


class CursoDetail(Resource):
    def get(self, id):
        curso = curso_service.Listar_cursos_id(id)
        if curso is None:
            return make_response(jsonify("curso nao foi encontrado"), 404)
        cs = curso_schemas.CursoSchema()
        return make_response(cs.jsonify(curso), 200)

    def put(self, id):
        curso_bd = curso_service.Listar_cursos_id(id)
        if curso_bd is None:
            return make_response(jsonify('curso nao encontrado'), 404)
        cs = curso_schemas.CursoSchema()
        validade = cs.validate(request.json)
        if validade:
            return make_response(jsonify(validade), 400)
        else:
            nome = request.json["nome"]
            descricao = request.json["descricao"]
            data_publicacao = request.json["data_publicacao"]
            formacao = request.json["formacao"]
            formacao_curso = formacao_services.listar_formacao_id(formacao)
            if formacao_curso is None:
                return make_response(jsonify("formacao nao foi encontrada"), 400)
            novo_curso = curso.Curso(nome=nome, descricao=descricao, data_publicacao=data_publicacao,
                                     formacao=formacao_curso)
            curso_service.atualiza_curso(curso_bd, novo_curso)
            curso_atualizado = curso_service.Listar_cursos_id(id)
            return make_response(cs.jsonify(curso_atualizado), 200)

    def delete(self, id):
        curso_bd = curso_service.Listar_cursos_id(id)
        if curso_bd is None:
            return make_response(jsonify("curso nao encontrado"), 404)
        curso_service.remove_curso(curso_bd)
        make_response("curso excluido com sucesso", 204)


api.add_resource(Cursolist, '/cursos')
api.add_resource(CursoDetail, '/cursos/<int:id>')
