from pydantic import BaseModel

class ItemIn(BaseModel):
    nome: str 
    descricao: str | None = ""
    id_package: int | None = None

class ItemUpdate(BaseModel):
    nome: str | None = None
    descricao: str | None = None
    id_package: int | None = None

class ItemOut(BaseModel):
    id_item: int 
    nome: str
    descricao: str 
    id_package: int | None = None
    status: bool 