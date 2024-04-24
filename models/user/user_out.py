from pydantic import BaseModel
from datetime import date
from .user import User

class UserOut(BaseModel):
    id_user: int 
    nome: str 
    sobrenome: str | None = None
    email: str
    data_criacao: date 
    status: bool 
