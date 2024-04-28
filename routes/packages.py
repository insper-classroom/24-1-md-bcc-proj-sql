from fastapi import APIRouter, HTTPException, status

from typing import List
from models.package.package import *
from db import DB

router = APIRouter()

@router.get("/packages/", response_model=List[PackageOut])
def list_package():
    return DB.getPackages()

@router.post("/packages/", response_model=PackageOut, status_code=status.HTTP_201_CREATED)
def create_package(packageIn: PackageIn):
    DB.checkUser(packageIn.id_user)
    package_dict = packageIn.model_dump()

    id = len(DB.packages)+1
    package_dict['id_package'] = id
    package = Package(**package_dict)
    DB.packages[id] = package

    return DB.getPackage(id)

@router.get("/packages/{package_id}", response_model=PackageOut)
def get_package(id_package: int):
    if id_package in DB.packages:
        return DB.getPackage(id_package)
    raise HTTPException(status_code=404, detail="Encomenda não encontrada")

@router.put("/packages/{package_id}", response_model=PackageOut)
def update_package(package_id: int, update: PackageUpdate):
    update_dict = update.model_dump()
    if package_id in DB.packages:
        if update_dict.id_user == DB.packages[package_id].id_user:
            # TODO: Buscar lista de produtos do pacote e adicionar o novo produto nela
            return "Tem que terminar a rota"
        return HTTPException(status_code=404, detail="Usuário Dono da Encomenda Incorreto")
    raise HTTPException(status_code=404, detail="Encomenda não encontrada")

@router.get("/packages/{package_id}/status")
async def update_package_status(package_id: int):
    if package_id in DB.packages:
        DB.packages[package_id].status = not DB.packages[package_id].status
        return DB.getPackage(package_id)
    return HTTPException(status_code=404, detail="Encomenda não encontrada")

@router.delete("/packages/{package_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_package(package_id: int):
    if package_id in DB.packages:
        del DB.packages[package_id]
        return {'message': 'Encomenda Deletada com Sucesso'}
    return HTTPException(status_code=404, detail="Encomenda não encontrada")