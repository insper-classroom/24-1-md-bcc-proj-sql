from fastapi import APIRouter, HTTPException, status # type: ignore
from typing import List
from models import Localizacao

localizacoes = [
    Localizacao(id_localizacao=1, logradouro="Rua A", cep="12345-678"),
    Localizacao(id_localizacao=2, logradouro="Rua B", cep="23456-789")
]

router = APIRouter()

@router.get("/localizacao", response_model=List[Localizacao])
def get_localizacao():
    return localizacoes

@router.post("/localizacao", response_model=Localizacao, status_code=status.HTTP_201_CREATED)
def nova_localizacao(localizacao: Localizacao):
    localizacoes.append(localizacao)
    return localizacao

@router.get("/localizacao/{id_localizacao}", response_model=Localizacao)
def get_localizacao(id_localizacao: int):
    localizacao = next(filter(lambda loc: loc.id_localizacao == id_localizacao, localizacoes), None)
    if localizacao:
        return localizacao
    raise HTTPException(status_code=404, detail="Localização não encontrada")

@router.put("/localizacao/{id_localizacao}", response_model=Localizacao)
def atualiza_localizacao(id_localizacao: int, localizacao: Localizacao):
    loc = next(filter(lambda loc: loc.id_localizacao == id_localizacao, localizacoes), None)
    if loc:
        loc.logradouro = localizacao.logradouro
        loc.cep = localizacao.cep
        return loc
    raise HTTPException(status_code=404, detail="Localização não encontrada")

@router.delete("/localizacao/{id_localizacao}", status_code=status.HTTP_204_NO_CONTENT)
def deleta_localizacao(id_localizacao: int):
    loc = next(filter(lambda loc: loc.id_localizacao == id_localizacao, localizacoes), None)
    if loc:
        localizacoes.remove(loc)
        return {"message": "Localização removida com sucesso"}
    raise HTTPException(status_code=404, detail="Localização não encontrada")