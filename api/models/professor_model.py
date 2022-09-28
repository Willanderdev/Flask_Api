from api import db


class Professor(db.Model):
    __tablename__ = "professor"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    nome = db.Column(db.String(50), nullable=False)
    idade = db.Column(db.Integer, nullable=False)
    formacoes = db.relationship("Formacao", secondary="professor_formacao", back_populates="professores")
