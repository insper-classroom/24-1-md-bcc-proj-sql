from fastapi import APIRouter, HTTPException, status # type: ignore
from typing import List
from models.movimentacao.movimentacao import *
from db import DB

from datetime import datetime

router = APIRouter()

@router.get("/movimentacao", response_model=List[Movimentacao])
def get_movimentacao():
    return DB.movimentacoes.values()

@router.post("/movimentacao", response_model=Movimentacao, status_code=status.HTTP_201_CREATED)
def nova_movimentacao(mov : MovimentacaoIn):
    id = len(DB.movimentacoes)+1
    mov = Movimentacao(
        id_movimentacao=id,
        id_encomenda=mov.id_encomenda,
        id_localizacao=mov.id_localizacao,
        status=mov.status,
        data=datetime.now()
    )
    
    DB.movimentacoes[id] = mov
    return mov

@router.get("/movimentacao/{id_encomenda}", response_model=List[Movimentacao])
def get_movimentacao(id_encomenda: int):
    movimentacoesDaEncomenda = list(filter(lambda mov: mov.id_encomenda == id_encomenda, DB.movimentacoes.values()))
    if len(movimentacoesDaEncomenda) > 0:
        return movimentacoesDaEncomenda
    raise HTTPException(status_code=404, detail="Nenhuma movimentação encontrada para a encomenda informada")

@router.get("/movimentacao/{id_encomenda}/{id_movimentacao}", response_model=Movimentacao)
def get_movimentacao(id_encomenda: int, id_movimentacao: int):
    movimentacao = next(filter(lambda mov: mov.id_encomenda == id_encomenda and mov.id_movimentacao == id_movimentacao, DB.movimentacoes.values()), None)
    if movimentacao:
        return movimentacao
    raise HTTPException(status_code=404, detail="Movimentação não encontrada")

@router.put("/movimentacao/{id_movimentacao}", response_model=Movimentacao)
def atualiza_movimentacao(id_movimentacao: int, mov: MovimentacaoUpdate):
    mov = DB.movimentacoes.get(id_movimentacao)
    if mov:
        mov.status = mov.status
        return mov
    raise HTTPException(status_code=404, detail="Movimentação não encontrada")

@router.delete("/movimentacao/{id_movimentacao}", status_code=status.HTTP_204_NO_CONTENT)
def deleta_movimentacao(id_movimentacao: int):
    mov = DB.movimentacoes.get(id_movimentacao)
    if mov:
        del DB.movimentacoes[id_movimentacao]
        return {"message": "Movimentação removida com sucesso"}
    raise HTTPException(status_code=404, detail="Movimentação não encontrada")