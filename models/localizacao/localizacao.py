from pydantic import BaseModel

class Localizacao(BaseModel):
    id_localizacao: int
    logradouro: str
    cep: str

class LocalizacaoIn(BaseModel):
    logradouro: str
    cep: str