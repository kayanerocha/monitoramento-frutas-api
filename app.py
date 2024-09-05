from decouple import config
from flask import Flask, jsonify, redirect
from flask_cors import CORS
from flask_migrate import Migrate
from flask_restful import Api, MethodNotAllowed, NotFound
from flask_swagger_ui import get_swaggerui_blueprint
from sys import argv

# from database.database import db
# from database.populate import *
# from models.estado import Estado
# from models.fruta import Fruta
# from models.loja import Loja
# from models.loja_fruta import LojaFruta
# from models.usuario import Usuario
# from models.notificacao import Notificacao
# from models.usuario_notificacao import UsuarioNotificacao
# from models.tipo_usuario import TipoUsuario
from resources.usuario import Usuario as UsuarioResource
from resources.swagger_config import SwaggerConfig
from util.commom import *

app = Flask(__name__)

# conexao = f'mysql+pymysql://{config("MYSQL_USER")}:{config("MYSQL_PASSWORD")}@{config("MYSQL_HOST")}/{config("MYSQL_DATABASE")}'
app.config['SECRET_KEY'] = config('SECRET_KEY')
# app.config['SQLALCHEMY_DATABASE_URI'] = conexao

# db.init_app(app)
# migrate = Migrate(app, db)
CORS(app)
api = Api(app, prefix=prefix, catch_all_404s=True)

# Swagger
build_swagger_config_json()
swaggerui_blueprint = get_swaggerui_blueprint(
    prefix,
    f'{config("PROTOCOL")}://{domain}{prefix}/swagger-config',
    config={
        'app_name': "Monitoramento de Frutas API",
        "layout": "BaseLayout",
        "docExpansion": "none"
    },
)
app.register_blueprint(swaggerui_blueprint)

# Error Handler
@app.errorhandler(NotFound)
def handle_method_not_found(e):
    response = jsonify({"message": str(e)})
    response.status_code = 404
    return response


@app.errorhandler(MethodNotAllowed)
def handle_method_not_allowed_error(e):
    response = jsonify({"message": str(e)})
    response.status_code = 405
    return response

api.add_resource(SwaggerConfig, '/swagger-config')
api.add_resource(UsuarioResource, '/usuarios')

# if 'populate' in argv:
#     db_load_estado_data(app, db)
#     db_load_fruta_data(app, db)
#     db_load_tipo_usuario(app, db)

# @app.route('/docs')
# def redirect_to_prefix():
#     if prefix != '':
#         return redirect(prefix)

if __name__ == '__main__':
    app.run(debug=True, port=80)