from fastapi import APIRouter, HTTPException, status # type: ignore
from typing import List
from models import Movimentacao

import datetime

router = APIRouter()

movimentacoes = [
    Movimentacao(id_movimentacao=1, id_encomenda=1, id_localizacao=1, status="Em trânsito", data=datetime.datetime.now()),
    Movimentacao(id_movimentacao=2, id_encomenda=1, id_localizacao=2, status="Em trânsito", data=datetime.datetime.now())
]

@router.get("/movimentacao", response_model=List[Movimentacao])
def get_movimentacao():
    return movimentacoes

@router.post("/movimentacao", response_model=Movimentacao, status_code=status.HTTP_201_CREATED)
def nova_movimentacao(mov : Movimentacao):
    movimentacoes.append(mov)
    return mov

@router.get("/movimentacao/{id_encomenda}", response_model=List[Movimentacao])
def get_movimentacao(id_encomenda: int):
    movimentacoesDaEncomenda = list(filter(lambda mov: mov.id_encomenda == id_encomenda, movimentacoes))
    if len(movimentacoesDaEncomenda) > 0:
        return movimentacoesDaEncomenda
    raise HTTPException(status_code=404, detail="Nenhuma movimentação encontrada para a encomenda informada")

@router.get("/movimentacao/{id_encomenda}/{id_movimentacao}", response_model=Movimentacao)
def get_movimentacao(id_encomenda: int, id_movimentacao: int):
    movimentacao = next(filter(lambda mov: mov.id_encomenda == id_encomenda and mov.id_movimentacao == id_movimentacao, movimentacoes), None)
    if movimentacao:
        return movimentacao
    raise HTTPException(status_code=404, detail="Movimentação não encontrada")

@router.put("/movimentacao/{id_movimentacao}", response_model=Movimentacao)
def atualiza_movimentacao(id_movimentacao: int, mov: Movimentacao):
    mov = next(filter(lambda mov: mov.id_movimentacao == id_movimentacao, movimentacoes), None)
    if mov:
        mov.status = mov.status
        return mov
    raise HTTPException(status_code=404, detail="Movimentação não encontrada")

@router.delete("/movimentacao/{id_movimentacao}", status_code=status.HTTP_204_NO_CONTENT)
def deleta_movimentacao(id_movimentacao: int):
    mov = next(filter(lambda mov: mov.id_movimentacao == id_movimentacao, movimentacoes), None)
    if mov:
        movimentacoes.remove(mov)
        return {"message": "Movimentação removida com sucesso"}
    raise HTTPException(status_code=404, detail="Movimentação não encontrada")