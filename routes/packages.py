from fastapi import APIRouter, HTTPException, status

from typing import List
from models.package.package import *
from db import DB

router = APIRouter()

@router.get("/packages/", response_model=List[PackageOut], tags=["packages"])
def list_package():
    """List all packages"""
    return DB.getPackages()

@router.post("/packages/", response_model=PackageOut, status_code=status.HTTP_201_CREATED, tags=["packages"])
def create_package(packageIn: PackageIn):
    """Creates a Package"""

    DB.checkUser(packageIn.id_user)
    package_dict = packageIn.model_dump()

    id = len(DB.packages)+1
    package_dict['id_package'] = id
    package = Package(**package_dict)
    DB.packages[id] = package

    return DB.getPackage(id)

@router.get("/packages/{package_id}", response_model=PackageOut, tags=["packages"])
def get_package(id_package: int):
    """Returns a Package given its id"""
    if id_package in DB.packages:
        return DB.getPackage(id_package)
    raise HTTPException(status_code=404, detail="Encomenda não encontrada")

@router.put("/packages/{package_id}", response_model=PackageOut, tags=["packages"])
def update_package(package_id: int, update: PackageUpdate):
    """Updates a Package's information"""
    update_dict = update.model_dump()
    DB.addItemToPackage(package_id, update_dict['id_item'])
    return DB.getPackage(package_id)

@router.get("/packages/{package_id}/status", tags=["packages"])
def update_package_status(package_id: int):
    """Updates a Package's Status (if it has been delivered or not)"""
    if package_id in DB.packages:
        DB.packages[package_id].status = not DB.packages[package_id].status
        return DB.getPackage(package_id)
    return HTTPException(status_code=404, detail="Encomenda não encontrada")

@router.delete("/packages/{package_id}", status_code=status.HTTP_204_NO_CONTENT, tags=["packages"])
def delete_package(package_id: int):
    """Deletes a Package's Information"""
    if package_id in DB.packages:
        del DB.packages[package_id]
        return {'message': 'Encomenda Deletada com Sucesso'}
    return HTTPException(status_code=404, detail="Encomenda não encontrada")