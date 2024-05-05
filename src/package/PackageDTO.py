from typing import List
from pydantic import BaseModel
from datetime import datetime

class PackageIn(BaseModel):
    id_user: int 

class PackageOut(BaseModel):
    id_package: int 
    id_user: int 
    data_criacao: datetime 
    status: bool 

class PackageUpdate(BaseModel):
    id_item: int