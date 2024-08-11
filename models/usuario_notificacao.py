from database.database import db

class UsuarioNotificacao(db.Model):
    __tablename__ = 'usuario_notificacao'
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.id'), primary_key=True)
    notificacao_id = db.Column(db.Integer, db.ForeignKey('notificacao.id'), primary_key=True)
    
    def __init__(self, usuario_id, notificacao_id) -> None:
        self.usuario_id = usuario_id
        self.notificacao_id = notificacao_id
    