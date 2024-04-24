from pydantic import BaseModel
from datetime import date
import datetime

class Package(BaseModel):
    id_package: int 
    id_user: int 
    data_criacao: date | None = datetime.datetime.now().date()
    status: bool | None = False