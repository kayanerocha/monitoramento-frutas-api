from sqlalchemy import TIMESTAMP
import datetime

from database.database import db

class Estado(db.Model):
    __tablename__ = 'estado'
    id = db.Column(db.Integer, primary_key=True)
    descricao = db.Column(db.String(50), nullable=False)
    created = db.Column(TIMESTAMP, default=datetime.datetime.now())
    frutas = db.relationship('Fruta', cascade='all,delete', backref='estado')
    
    def __init__(self, descricao) -> None:
        self.descricao = descricao
        