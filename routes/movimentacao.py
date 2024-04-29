from fastapi import APIRouter, HTTPException, status # type: ignore
from typing import List
from models.movimentacao.movimentacao import *
from db import DB

from datetime import datetime

router = APIRouter()

@router.get("/movimentacao", response_model=List[Movimentacao], tags=["movimentacao"])
def get_movimentacao(id_encomenda: int = None, id_movimentacao: int = None): 
    """Returns a Specific Movimentação based on the id for the move and the Package id"""
    if id_movimentacao:
        movimentacao = DB.getMovimentacao(id_movimentacao)
        if movimentacao:
            return [movimentacao]
        raise HTTPException(status_code=404, detail="Movimentação não encontrada")
    
    if id_encomenda:
        movimentacoesDaEncomenda = list(filter(lambda mov: mov.id_encomenda == id_encomenda, DB.movimentacoes.values()))
        if len(movimentacoesDaEncomenda) > 0:
            return movimentacoesDaEncomenda
        raise HTTPException(status_code=404, detail="Nenhuma movimentação encontrada para a encomenda informada")

    return DB.getMovimentacoes()

@router.post("/movimentacao", response_model=Movimentacao, status_code=status.HTTP_201_CREATED, tags=["movimentacao"])
def nova_movimentacao(movIn : MovimentacaoIn):
    """Creates a New Movimentação"""
    DB.checkPackage(movIn.id_encomenda)
    mov_dict = movIn.model_dump()
    mov_dict['id_movimentacao'] = DB.movimentacoesNextID
    DB.movimentacoesIncID()
    mov_dict['data'] = datetime.now()
    mov = Movimentacao(**mov_dict)
    DB.movimentacoes[mov.id_movimentacao] = mov
    return mov

@router.put("/movimentacao/{id_movimentacao}", response_model=Movimentacao, tags=["movimentacao"])
def atualiza_movimentacao(id_movimentacao: int, movUpdate: MovimentacaoUpdate):
    """Updates a Movimentação's Status (where the package is in relation to the delivery pipeline)"""
    mov = DB.movimentacoes.get(id_movimentacao)
    if mov:
        mov.status = movUpdate.status
        return mov
    raise HTTPException(status_code=404, detail="Movimentação não encontrada")

@router.delete("/movimentacao/{id_movimentacao}", status_code=status.HTTP_204_NO_CONTENT, tags=["movimentacao"])
def deleta_movimentacao(id_movimentacao: int):
    """Deletes a Movimentação's information"""
    mov = DB.movimentacoes.get(id_movimentacao)
    if mov:
        del DB.movimentacoes[id_movimentacao]
        return {"message": "Movimentação removida com sucesso"}
    raise HTTPException(status_code=404, detail="Movimentação não encontrada")