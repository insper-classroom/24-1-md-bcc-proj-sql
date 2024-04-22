from fastapi import APIRouter, HTTPException, status # type: ignore
from typing import List
from db import DB
from models.localizacao.localizacao import *

router = APIRouter()

@router.get("/localizacao", response_model=List[Localizacao])
def get_localizacao():
    return DB.localizacoes.values()

@router.post("/localizacao", response_model=Localizacao, status_code=status.HTTP_201_CREATED)
def nova_localizacao(loc: LocalizacaoIn):
    id = len(DB.localizacoes)+1
    loc = Localizacao(
        id_localizacao=id,
        logradouro=loc.logradouro,
        cep=loc.cep
    )
    DB.localizacoes[id] = loc
    return loc

@router.get("/localizacao/{id_localizacao}", response_model=Localizacao)
def get_localizacao(id_localizacao: int):
    loc = DB.localizacoes.get(id_localizacao)
    if loc:
        return loc
    raise HTTPException(status_code=404, detail="Localização não encontrada")

@router.put("/localizacao/{id_localizacao}", response_model=Localizacao)
def atualiza_localizacao(id_localizacao: int, localizacao: LocalizacaoIn):
    loc = DB.localizacoes.get(id_localizacao)
    if loc:
        loc.logradouro = localizacao.logradouro
        loc.cep = localizacao.cep
        return loc
    raise HTTPException(status_code=404, detail="Localização não encontrada")

@router.delete("/localizacao/{id_localizacao}", status_code=status.HTTP_204_NO_CONTENT)
def deleta_localizacao(id_localizacao: int):
    loc = DB.localizacoes.get(id_localizacao)
    if loc:
        del DB.localizacoes[id_localizacao]
        return {"message": "Localização removida com sucesso"}
    raise HTTPException(status_code=404, detail="Localização não encontrada")