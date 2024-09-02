from sqlalchemy import TIMESTAMP
import datetime

from database.database import db

class Fruta(db.Model):
    __tablename__ = 'fruta'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50), nullable=False)
    estado_id = db.Column(db.Integer, db.ForeignKey('estado.id'))
    created = db.Column(TIMESTAMP, default=datetime.datetime.now())
    
    def __init__(self, nome, estado_id) -> None:
        self.nome = nome
        self.estado_id = estado_id