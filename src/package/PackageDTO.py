from typing import List
from pydantic import BaseModel
from datetime import date

from models.item.item import Item

class PackageIn(BaseModel):
    id_user: int 

class PackageOut(BaseModel):
    id_package: int 
    id_user: int 
    data_criacao: date 
    status: bool 
