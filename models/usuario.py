from sqlalchemy import TIMESTAMP
import datetime

from database.database import db
from models.usuario_notificacao import UsuarioNotificacao

class Usuario(db.Model):
    __tablename__ = 'usuario'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    matricula = db.Column(db.String(50))
    email = db.Column(db.String(100), nullable=False)
    senha = db.Column(db.String(255), nullable=False)
    created = db.Column(TIMESTAMP, default=datetime.datetime.now())
    loja_id = db.Column(db.Integer, db.ForeignKey('loja.id'))
    notificacoes = db.relationship('Notificacao', secondary=UsuarioNotificacao.__table__, backref='usuarios')
    tipo_usuario_id = db.Column(db.Integer, db.ForeignKey('tipo_usuario.id'))
    ativo = db.Column(db.Boolean, nullable=False)
    
    def __init__(self, nome, matricula, email, senha, tipo_usuario_id, loja_id=None) -> None:
        self.nome = nome
        self.matricula = matricula
        self.email = email
        self.senha = senha
        self.loja_id = loja_id
        self.tipo_usuario_id = tipo_usuario_id
        self.ativo = 0
    