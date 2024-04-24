from pydantic import BaseModel

class ItemUpdate(BaseModel):
    nome: str | None = None
    descricao: str | None = None
    id_package: int | None = None
