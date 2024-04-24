from typing import List
from pydantic import BaseModel
from datetime import date
import datetime

from models.item.item import Item

class Package(BaseModel):
    id_package: int 
    id_user: int 
    data_criacao: date | None = datetime.datetime.now().date()
    status: bool | None = False

class PackageIn(BaseModel):
    id_user: int 

class PackageUpdate(BaseModel):
    id_user: int 
    id_item: int

class PackageOut(BaseModel):
    id_package: int 
    id_user: int 
    data_criacao: date 
    status: bool 
    produtos: List[Item] | None = []