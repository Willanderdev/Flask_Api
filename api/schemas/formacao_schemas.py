from api import ma
from ..models import formacao_model
from marshmallow import fields
from ..schemas import curso_schemas, professor_schemas


class FormacaoSchema(ma.SQLAlchemyAutoSchema):
    professores = ma.Nested(professor_schemas.ProfessorSchema, many=True)
    class Meta:
        model = formacao_model.Formacao
        load_instance = True
        fields = ("id", "nome", "descricao", "professores")

    nome = fields.String(required=True)
    descricao = fields.String(required=True)
    cursos = fields.List(fields.Nested(curso_schemas.CursoSchema, only=('id', 'nome')))
    