from pydantic import BaseModel
from datetime import date
import datetime

class Item(BaseModel):
    id_item: int 
    nome: str
    data_criacao: date | None = datetime.datetime.now().date()
    descricao: str 
    id_package: int | None = None
    status: bool | None = True

class ItemIn(BaseModel):
    nome: int 
    descricao: str | None = ""

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