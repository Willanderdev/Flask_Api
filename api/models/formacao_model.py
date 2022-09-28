from api import db
from .professor_model import Professor

professor_formacao = db.Table('professor_formacao',
db.Column('professor_id', db.Integer, db.ForeignKey('professor.id'), primary_key=True, nullable=False),
db.Column('formacao_id', db.Integer, db.ForeignKey('formacao.id'), primary_key=True, nullable=False),
                              )

class Formacao(db.Model):
    __tablename__ = "formacao"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    nome = db.Column(db.String(50), nullable=False)
    descricao = db.Column(db.String(100), nullable=False)
    professores = db.relationship(Professor, secondary="professor_formacao", back_populates="formacoes")
