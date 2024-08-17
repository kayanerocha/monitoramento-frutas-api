from flask import Blueprint, request
from werkzeug.security import generate_password_hash

from database.database import db
from models.usuario import Usuario
from models.tipo_usuario import TipoUsuario

usuario_blueprint = Blueprint('usuario', __name__)

@usuario_blueprint.route('/cadastro-usuario', methods=['POST'])
def cadastro():
    response = {
        'message': '',
    }
    
    try:
        data = request.get_json()
        nome = data['nome']
        matricula = data['matricula']
        email = data['email']
        senha = data['senha']
        tipo_usuario = data['tipo_usuario']
        tipo_usuario_id = TipoUsuario.query.filter_by(descricao=tipo_usuario).first().id
    except Exception:
        response['message'] = 'É necessário enviar um json com os campos "nome", "matricula", "email", "senha" e "tipo_usuario".'
        return response
    
    usuario = Usuario.query.filter_by(email=email).first()
    
    
    if len(senha) <= 5:
        response['message'] = 'A senha precisa ter 6 ou mais caracteres.'
    elif usuario:
        response['message'] = 'Usuário já cadastrado.'
    else:
        hash_senha = generate_password_hash(senha)
        novo_usuario = Usuario(nome, matricula, email, hash_senha, tipo_usuario_id)
        
        db.session.add(novo_usuario)
        db.session.commit()
        
        response['message'] = 'Usuário cadastrado com sucesso.'
    return response
        
    