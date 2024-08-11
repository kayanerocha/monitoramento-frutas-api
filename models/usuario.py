from sqlalchemy import TIMESTAMP
import datetime

from database.database import db
from models.usuario_notificacao import UsuarioNotificacao

class Usuario(db.Model):
    __tablename__ = 'usuario'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    matricula = db.Column(db.String(50))
    created = db.Column(TIMESTAMP, default=datetime.datetime.now())
    loja_id = db.Column(db.Integer, db.ForeignKey('loja.id'))
    notificacoes = db.relationship('Notificacao', secondary=UsuarioNotificacao.__table__, backref='usuarios')
    
    def __init__(self, nome, matricula, loja_id) -> None:
        self.nome = nome
        self.matricula = matricula
        self.loja_id = loja_id
    