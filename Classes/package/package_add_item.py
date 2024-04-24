from pydantic import BaseModel


class PackageUpdate(BaseModel):
    id_user: int 
    id_item: int
