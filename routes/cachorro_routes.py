from flask import Blueprint, request, jsonify
from controllers.cachorro_controller import criar_cachorro, listar_cachorros

cachorro_routes = Blueprint('cachorro_routes', __name__)

# POST - cadastrar cachorro
@cachorro_routes.route('/cachorros', methods=['POST'])
def cadastrar():
    data = request.get_json()
    cachorro = criar_cachorro(data)
    return jsonify(cachorro), 201

# GET - listar cachorros
@cachorro_routes.route('/cachorros', methods=['GET'])
def listar():
    cachorros = listar_cachorros()
    return jsonify(cachorros), 200