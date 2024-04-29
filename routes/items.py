from fastapi import APIRouter, HTTPException, status

from typing import List
from models.item.item import *
from db import DB

router = APIRouter()

@router.get("/items/", response_model=List[ItemOut])
def list_items():
    return DB.getItems()

@router.post("/items/", response_model=ItemOut, status_code=status.HTTP_201_CREATED)
def create_items(itemsIn: ItemIn):
    if itemsIn.id_package:
        DB.checkPackage(itemsIn.id_package)

    items_dict = itemsIn.model_dump()
    id = len(DB.items)+1
    items_dict['id_item'] = id
    item = Item(**items_dict)
    DB.items[id] = item

    return DB.getItem(id)

@router.get("/items/{items_id}", response_model=ItemOut)
def get_items(items_id: int):
    if items_id in DB.items:
        return DB.getItem(items_id)
    raise HTTPException(status_code=404, detail="Item da encomenda não encontrada")

@router.put("/items/{items_id}")
def update_items(items_id: int, update: ItemUpdate):
    update_dict = update.model_dump()
    if items_id in DB.items:

        if update_dict['nome'] is not None:
            DB.items[items_id].nome = update_dict['nome']

        if update_dict['descricao'] is not None:
            DB.items[items_id].descricao = update_dict['descricao']

        if update_dict['id_package'] is not None:
            DB.items[items_id].id_package = update_dict['id_package']

        return DB.getItem(items_id)
    raise HTTPException(status_code=404, detail="Item da encomenda não encontrada")

@router.put("/items/{items_id}/status")
def update_items_status(items_id: int):
    if items_id in DB.items:
        DB.items[items_id].status = not DB.items[items_id].status
        return DB.getItem(items_id)
    raise HTTPException(status_code=404, detail="Item da encomenda não encontrada")

@router.delete("/items/{items_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_items(items_id: int):
    if items_id in DB.items:
        del DB.items[items_id]
        return {'message': 'Item da encomenda Deletada com Sucesso'}
    raise HTTPException(status_code=404, detail="Item da encomenda não encontrada")