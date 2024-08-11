from sqlalchemy import TIMESTAMP
import datetime

from database.database import db
from models.loja_fruta import LojaFruta

class Loja(db.Model):
    __tablename__ = 'loja'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    razao_social = db.Column(db.String(100), nullable=False)
    cnpj = db.Column(db.String(14), nullable=False)
    created = db.Column(TIMESTAMP, default=datetime.datetime.now())
    frutas = db.relationship('Fruta', secondary=LojaFruta.__table__, backref='lojas')
    usuarios = db.relationship('Usuario', backref='loja')
    
    def __init__(self, nome, razao_social, cnpj) -> None:
        self.nome = nome
        self.razao_social = razao_social
        self.cnpj = cnpj
    
    