from pydantic import BaseModel
from datetime import date
from typing import List

from Classes.item.item import Item

class PackageOut(BaseModel):
    id_package: int 
    id_user: int 
    data_criacao: date 
    status: bool 
    produtos: List[Item] | None = []