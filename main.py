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

movimentacoes = [
    Movimentacao(id_movimentacao=1, id_encomenda=1, id_localizacao=1, status="Em trânsito", data=datetime.datetime.now()),
    Movimentacao(id_movimentacao=2, id_encomenda=1, id_localizacao=2, status="Em trânsito", data=datetime.datetime.now())
]


@app.get("/")
def root():
    return {"Hello": "World"}




