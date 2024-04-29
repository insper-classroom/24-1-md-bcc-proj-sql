from fastapi import APIRouter, HTTPException, status # type: ignore
from typing import List
from models.movimentacao.movimentacao import *
from db import DB

from datetime import datetime

router = APIRouter()

@router.get("/movimentacao", response_model=List[Movimentacao])
def get_movimentacao(id_encomenda: int = None, id_movimentacao: int = None): 
    if id_movimentacao and id_movimentacao:
        movimentacao = next(filter(lambda mov: mov.id_encomenda == id_encomenda and mov.id_movimentacao == id_movimentacao, DB.movimentacoes.values()), None)
        if movimentacao:
            return [movimentacao]
        raise HTTPException(status_code=404, detail="Movimentação não encontrada")
    
    if id_encomenda:
        movimentacoesDaEncomenda = list(filter(lambda mov: mov.id_encomenda == id_encomenda, DB.movimentacoes.values()))
        if len(movimentacoesDaEncomenda) > 0:
            return movimentacoesDaEncomenda
        raise HTTPException(status_code=404, detail="Nenhuma movimentação encontrada para a encomenda informada")

    if id_movimentacao:
        movimentacao = next(filter(lambda mov: mov.id_movimentacao == id_movimentacao, DB.movimentacoes.values()), None)
        if movimentacao:
            return [movimentacao]
        raise HTTPException(status_code=404, detail="Movimentação não encontrada")

    return DB.getMovimentacoes()

@router.post("/movimentacao", response_model=Movimentacao, status_code=status.HTTP_201_CREATED)
def nova_movimentacao(movIn : MovimentacaoIn):
    DB.checkPackage(movIn.id_encomenda)
    mov_dict = movIn.model_dump()
    mov_dict['id_movimentacao'] = len(DB.movimentacoes) + 1
    mov_dict['data'] = datetime.now()
    mov = Movimentacao(**mov_dict)
    DB.movimentacoes[mov.id_movimentacao] = mov
    return mov

@router.put("/movimentacao/{id_movimentacao}", response_model=Movimentacao)
def atualiza_movimentacao(id_movimentacao: int, movUpdate: MovimentacaoUpdate):
    mov = DB.movimentacoes.get(id_movimentacao)
    if mov:
        mov.status = movUpdate.status
        return mov
    raise HTTPException(status_code=404, detail="Movimentação não encontrada")

@router.delete("/movimentacao/{id_movimentacao}", status_code=status.HTTP_204_NO_CONTENT)
def deleta_movimentacao(id_movimentacao: int):
    mov = DB.movimentacoes.get(id_movimentacao)
    if mov:
        del DB.movimentacoes[id_movimentacao]
        return {"message": "Movimentação removida com sucesso"}
    raise HTTPException(status_code=404, detail="Movimentação não encontrada")