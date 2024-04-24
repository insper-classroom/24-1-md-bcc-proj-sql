from pydantic import BaseModel


class ItemOut(BaseModel):
    id_item: int 
    nome: str
    descricao: str 
    id_package: int | None = None
    status: bool 