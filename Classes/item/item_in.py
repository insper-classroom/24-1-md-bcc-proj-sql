from pydantic import BaseModel


class ItemIn(BaseModel):
    nome: int 
    descricao: str | None = ""
