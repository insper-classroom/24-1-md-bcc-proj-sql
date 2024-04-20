# run: uvicorn main:app --reload

from fastapi import FastAPI, HTTPException, status # type: ignore
from typing import List
import datetime
from pydantic import BaseModel

app = FastAPI()

class Movimentacao(BaseModel):
    id_movimentacao: int
    id_encomenda: int
    id_localizacao: int
    status: str
    data: datetime.datetime

class Localizacao(BaseModel):
    id_localizacao: int
    logradouro: str
    cep: str

movimentacoes = [
    Movimentacao(id_movimentacao=1, id_encomenda=1, id_localizacao=1, status="Em trânsito", data=datetime.datetime.now()),
    Movimentacao(id_movimentacao=2, id_encomenda=1, id_localizacao=2, status="Em trânsito", data=datetime.datetime.now())
]

localizacoes = [
    Localizacao(id_localizacao=1, logradouro="Rua A", cep="12345-678"),
    Localizacao(id_localizacao=2, logradouro="Rua B", cep="23456-789")
]

@app.get("/")
def root():
    return {"Hello": "World"}

@app.get("/movimentacao", response_model=List[Movimentacao])
def get_movimentacao():
    return movimentacoes

@app.post("/movimentacao", response_model=Movimentacao, status_code=status.HTTP_201_CREATED)
def nova_movimentacao(mov : Movimentacao):
    movimentacoes.append(mov)
    return mov

@app.get("/movimentacao/{id_encomenda}", response_model=List[Movimentacao])
def get_movimentacao(id_encomenda: int):
    movimentacoesDaEncomenda = list(filter(lambda mov: mov.id_encomenda == id_encomenda, movimentacoes))
    if len(movimentacoesDaEncomenda) > 0:
        return movimentacoesDaEncomenda
    raise HTTPException(status_code=404, detail="Nenhuma movimentação encontrada para a encomenda informada")

@app.get("/movimentacao/{id_encomenda}/{id_movimentacao}", response_model=Movimentacao)
def get_movimentacao(id_encomenda: int, id_movimentacao: int):
    movimentacao = next(filter(lambda mov: mov.id_encomenda == id_encomenda and mov.id_movimentacao == id_movimentacao, movimentacoes), None)
    if movimentacao:
        return movimentacao
    raise HTTPException(status_code=404, detail="Movimentação não encontrada")

@app.put("/movimentacao/{id_movimentacao}", response_model=Movimentacao)
def atualiza_movimentacao(id_movimentacao: int, mov: Movimentacao):
    mov = next(filter(lambda mov: mov.id_movimentacao == id_movimentacao, movimentacoes), None)
    if mov:
        mov.status = mov.status
        return mov
    raise HTTPException(status_code=404, detail="Movimentação não encontrada")

@app.delete("/movimentacao/{id_movimentacao}", status_code=status.HTTP_204_NO_CONTENT)
def deleta_movimentacao(id_movimentacao: int):
    mov = next(filter(lambda mov: mov.id_movimentacao == id_movimentacao, movimentacoes), None)
    if mov:
        movimentacoes.remove(mov)
        return {"message": "Movimentação removida com sucesso"}
    raise HTTPException(status_code=404, detail="Movimentação não encontrada")

@app.get("/localizacao", response_model=List[Localizacao])
def get_localizacao():
    return localizacoes

@app.post("/localizacao", response_model=Localizacao, status_code=status.HTTP_201_CREATED)
def nova_localizacao(localizacao: Localizacao):
    localizacoes.append(localizacao)
    return localizacao

@app.get("/localizacao/{id_localizacao}", response_model=Localizacao)
def get_localizacao(id_localizacao: int):
    localizacao = next(filter(lambda loc: loc.id_localizacao == id_localizacao, localizacoes), None)
    if localizacao:
        return localizacao
    raise HTTPException(status_code=404, detail="Localização não encontrada")

@app.put("/localizacao/{id_localizacao}", response_model=Localizacao)
def atualiza_localizacao(id_localizacao: int, localizacao: Localizacao):
    loc = next(filter(lambda loc: loc.id_localizacao == id_localizacao, localizacoes), None)
    if loc:
        loc.logradouro = localizacao.logradouro
        loc.cep = localizacao.cep
        return loc
    raise HTTPException(status_code=404, detail="Localização não encontrada")

@app.delete("/localizacao/{id_localizacao}", status_code=status.HTTP_204_NO_CONTENT)
def deleta_localizacao(id_localizacao: int):
    loc = next(filter(lambda loc: loc.id_localizacao == id_localizacao, localizacoes), None)
    if loc:
        localizacoes.remove(loc)
        return {"message": "Localização removida com sucesso"}
    raise HTTPException(status_code=404, detail="Localização não encontrada")