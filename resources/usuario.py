from flask import request
from flask_restful import Resource, marshal_with, fields
from werkzeug.security import generate_password_hash

from database.database import db
from models.usuario import Usuario as UsuarioModel
from models.tipo_usuario import TipoUsuario

usuario_campos = {
    'id': fields.Integer,
    'nome': fields.String,
    'matricula': fields.String,
    'email': fields.String,
    'created': fields.DateTime,
    'loja': fields.String,
    'tipo_usuario': fields.Integer,
    'ativo': fields.Integer
}

class Usuario(Resource):
    @marshal_with(usuario_campos)
    def get(self):
        usuarios = db.session.query(
            UsuarioModel.id, UsuarioModel.nome, UsuarioModel.matricula, UsuarioModel.email, UsuarioModel.ativo,
            UsuarioModel.created).all()
        return usuarios
    
    def post(self):
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
        except Exception as e:
            response['message'] = f'É necessário enviar um json com os campos "nome", "matricula", "email", "senha" e "tipo_usuario". {e}'
            return response
        
        tipo_usuario_id = TipoUsuario.query.filter_by(descricao=tipo_usuario).first().id
        usuario = UsuarioModel.query.filter_by(email=email).first()
        
        
        if len(senha) <= 5:
            response['message'] = 'A senha precisa ter 6 ou mais caracteres.'
        elif usuario:
            response['message'] = 'Usuário já cadastrado.'
        else:
            hash_senha = generate_password_hash(senha)
            novo_usuario = UsuarioModel(nome, matricula, email, hash_senha, tipo_usuario_id)
            
            db.session.add(novo_usuario)
            db.session.commit()
            
            response['message'] = 'Usuário cadastrado com sucesso.'
        return response