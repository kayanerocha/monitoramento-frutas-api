from distutils.log import debug
from decouple import config
from flask import Flask
from flask_migrate import Migrate
from sys import argv

from blueprints.usuario import usuario_blueprint
from database.database import db
from database.populate import *
from models.estado import Estado
from models.fruta import Fruta
from models.loja import Loja
from models.loja_fruta import LojaFruta
from models.usuario import Usuario
from models.notificacao import Notificacao
from models.usuario_notificacao import UsuarioNotificacao
from models.tipo_usuario import TipoUsuario

app = Flask(__name__)

conexao = f'mysql+pymysql://{config("MYSQL_USER")}:{config("MYSQL_PASSWORD")}@{config("MYSQL_HOST")}/{config("MYSQL_DATABASE")}'
app.config['SECRET_KEY'] = config('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = conexao

db.init_app(app)
migrate = Migrate(app, db)

app.register_blueprint(usuario_blueprint)

if 'populate' in argv:
    db_load_estado_data(app, db)
    db_load_fruta_data(app, db)
    db_load_tipo_usuario(app, db)

@app.route('/', methods=['GET'])
def hello():
    return 'Hello, world!'

if __name__ == '__main__':
    app.run(debug=True)