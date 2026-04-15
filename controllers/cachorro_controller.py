from models.cachorro_model import Cachorro
from db import db

# Criar cachorro
def criar_cachorro(data):
    novo = Cachorro(
        nome=data["nome"],
        raca=data["raca"],
        idade=data["idade"]
    )
    db.session.add(novo)
    db.session.commit()
    return novo.to_dict()

# Listar cachorros
def listar_cachorros():
    cachorros = Cachorro.query.all()
    return [c.to_dict() for c in cachorros]