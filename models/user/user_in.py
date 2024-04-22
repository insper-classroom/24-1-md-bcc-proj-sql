from pydantic import BaseModel

class UserIn(BaseModel):
    nome: str | None = None
    sobrenome: str | None = None
    senha: str
    email: str