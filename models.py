from pydantic import BaseModel
import datetime

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