from database.database import db

class TipoUsuario(db.Model):
    __tablename__ = 'tipo_usuario'
    id = db.Column(db.Integer, primary_key=True)
    descricao = db.Column(db.String(20), nullable=False)
    usuarios = db.relationship('Usuario', backref='tipo_usuario')
    
    def __init__(self, descricao) -> None:
        self.descricao = descricao