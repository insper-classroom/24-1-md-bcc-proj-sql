from models.movimentacao.movimentacao import Movimentacao
from models.localizacao.localizacao import Localizacao
from models.user.user import User

import datetime

class DB:
    movimentacoes = {
        1: Movimentacao(id_movimentacao=1, id_encomenda=1, id_localizacao=1, status="Em trânsito", data=datetime.datetime.now()),
        2: Movimentacao(id_movimentacao=2, id_encomenda=1, id_localizacao=2, status="Em trânsito", data=datetime.datetime.now())
    }

    localizacoes = {
        1: Localizacao(id_localizacao=1, logradouro="Rua A", cep="12345-678"),
        2: Localizacao(id_localizacao=2, logradouro="Rua B", cep="23456-789")
    }

    users = {

    }