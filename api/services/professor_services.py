from ..models import professor_model
from api import db


def cadastrar_professor(professor):
    professor_bd = professor_model.Professor(nome=professor.nome, idade=professor.idade)
    db.session.add(professor_bd)
    db.session.commit()
    return professor_bd


def listarprofessores():
    professores = professor_model.Professor.query.all()
    return professores


def Listar_professor_id(id):
    professor = professor_model.Professor.query.filter_by(id=id).first()
    return professor


def atualiza_professor(professor_anterior, professor_novo):
    professor_anterior.nome = professor_novo.nome
    professor_anterior.idade = professor_novo.idade
    db.session.commit()


def remove_professor(professor):
    db.session.delete(professor)
    db.session.commit()