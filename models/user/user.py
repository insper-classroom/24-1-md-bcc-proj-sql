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

class UserUpdateSenha(BaseModel):
    senha: str 
    senha_nova: str

class UserOut(BaseModel):
    id_user: int 
    nome: str 
    sobrenome: str | None = None
    email: str
    data_criacao: date 
    status: bool 

class UserIn(BaseModel):
    nome: str | None = None
    sobrenome: str | None = None
    senha: str
    email: str