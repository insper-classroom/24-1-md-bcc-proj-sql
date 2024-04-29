from pydantic import BaseModel
import datetime

class Movimentacao(BaseModel):
    id_movimentacao: int
    id_encomenda: int
    endereco: str
    status: str
    data: datetime.datetime

class MovimentacaoIn(BaseModel):
    id_encomenda: int
    endereco: str
    status: str

class MovimentacaoUpdate(BaseModel):
    status: str