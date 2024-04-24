from pydantic import BaseModel
from datetime import date
import datetime

class User(BaseModel):
    id_user: int 
    nome: str | None = None
    sobrenome: str | None = None
    senha: str
    email: str
    data_criacao: date | None = datetime.datetime.now().date()
    status: bool | None = True