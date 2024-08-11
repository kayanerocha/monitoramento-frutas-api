from sqlalchemy.sql import text as sa_text

from models.estado import Estado
from models.fruta import Fruta

def db_load_estado_data(app, db):
    volume_baixo = Estado(descricao='Volume Baixo')
    abastecido = Estado(descricao='Abastecido')
    
    with app.app_context():
        db.session.add(volume_baixo)
        db.session.add(abastecido)
        db.session.commit()

def db_load_fruta_data(app, db):
    banana = Fruta(nome='Banana', estado_id=1)
    laranja = Fruta(nome='Laranja', estado_id=2)
    maca = Fruta(nome='Maçã', estado_id=1)
    
    with app.app_context():
        db.session.add(banana)
        db.session.add(laranja)
        db.session.add(maca)
        db.session.commit()