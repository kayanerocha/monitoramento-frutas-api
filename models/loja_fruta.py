from database.database import db

class LojaFruta(db.Model):
    __tablename__ = 'loja_fruta'
    loja_id = db.Column(db.Integer, db.ForeignKey('loja.id'), primary_key=True)
    fruta_id = db.Column(db.Integer, db.ForeignKey('fruta.id'), primary_key=True)
    
    def __init__(self, loja_id, fruta_id) -> None:
        self.loja_id = loja_id
        self.fruta_id = fruta_id