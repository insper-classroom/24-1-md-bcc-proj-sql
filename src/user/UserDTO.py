from pydantic import BaseModel
from datetime import date

class UserUpdateSenha(BaseModel):
    senha: str 
    senha_antiga: str

class UserOut(BaseModel):
    id_user: int 
    nome: str 
    sobrenome: str | None = None
    email: str
    status: bool 

class UserIn(BaseModel):
    nome: str | None = None
    sobrenome: str | None = None
    senha: str
    email: str