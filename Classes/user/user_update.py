from pydantic import BaseModel


class UserUpdateSenha(BaseModel):
    senha: str 
    senha_nova: str

