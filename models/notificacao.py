from sqlalchemy import TIMESTAMP
import datetime

from database.database import db

class Notificacao(db.Model):
    __tablename__ = 'notificacao'
    id = db.Column(db.Integer, primary_key=True)
    mensagem = db.Column(db.String(500), nullable=False)
    created = db.Column(TIMESTAMP, default=datetime.datetime.now())
    