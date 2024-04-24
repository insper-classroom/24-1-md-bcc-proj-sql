from fastapi import APIRouter, HTTPException, status

from typing import List, Dict

from models.package.package import *



router = APIRouter()

packages = {}

@router.get("/packages/", response_model=Dict[int, Package])
def list_package():
    return packages


@router.post("/packages/", response_model=PackageOut, status_code=status.HTTP_201_CREATED)
async def create_package(packageIn: PackageIn):
    package_dict = packageIn.model_dump()

    package_dict['id_package'] = len(packages)
    package = Package(**package_dict)
    packages[package.id_package] = package

    packageOut = packageOut(
        id_package=package.id_package,
        id_user=package.id_user,
        data_criacao=package.data_criacao,
        status=package.status
        # TODO: Criar a chamada pros produtos e ver quais estão atrelados ao pacote
    )

    return packageOut


@router.get("/packages/{package_id}", response_model=PackageOut)
def get_package(package_id: int):
    if package_id in packages:
        return packages[package_id]
    return HTTPException(status_code=404, detail="Encomenda não encontrada")


@router.put("/packages/{package_id}")
async def update_package(package_id: int, update: PackageUpdate):
    update_dict = update.model_dump()
    if package_id in packages:

        if update_dict.id_user == packages[package_id].id_user:
            # TODO: Buscar lista de produtos do pacote e adicionar o novo produto nela
        
            return "Tem que terminar a rota"
        
        return HTTPException(status_code=404, detail="Usuário Dono da Encomenda Incorreto")


    return HTTPException(status_code=404, detail="Encomenda não encontrada")


@router.get("/packages/{package_id}/status")
async def update_package_status(package_id: int):
    if package_id in packages:

        packages[package_id].status = not packages[package_id].status
        
        return packages[package_id]

    return HTTPException(status_code=404, detail="Encomenda não encontrada")


@router.delete("/packages/{package_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_package(package_id: int):
    if package_id in packages:

        del packages[package_id]
        
        return {'message': 'Encomenda Deletada com Sucesso'}

    return HTTPException(status_code=404, detail="Encomenda não encontrada")