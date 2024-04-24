from fastapi import APIRouter, HTTPException, status

from typing import List, Dict

from Classes.item.item import Item
from Classes.item.item_in import ItemIn
from Classes.item.item_out import ItemOut
from Classes.item.item_update import ItemUpdate


router = APIRouter()

items = {}

@router.get("/items/", response_model=Dict[int, items])
def list_items():
    return items


@router.post("/items/", response_model=ItemOut, status_code=status.HTTP_201_CREATED)
async def create_items(itemsIn: ItemIn):
    items_dict = itemsIn.model_dump()

    items_dict['id_item'] = len(items)
    item = Item(**items_dict)
    items[item.id_items] = item

    itemsOut = ItemOut(
        id_item=item.id_item,
        nome=item.nome,
        descricao=item.descricao,
        status=item.status
    )

    return itemsOut


@router.get("/items/{items_id}", response_model=ItemOut)
def get_items(items_id: int):
    if items_id in items:

        item = items[items_id]
        itemsOut = ItemOut(
            id_item=item.id_item,
            nome=item.nome,
            descricao=item.descricao,
            id_package=item.id_package,
            status=item.status
        )

        return itemsOut
    return HTTPException(status_code=404, detail="Encomenda não encontrada")


@router.put("/items/{items_id}")
async def update_items(items_id: int, update: ItemUpdate):
    update_dict = update.model_dump()
    if items_id in items:
        
        if update_dict['nome'] is not None:
            items[items_id].nome = update_dict['nome']

        if update_dict['descricao'] is not None:
            items[items_id].descricao = update_dict['descricao']

        if update_dict['id_package'] is not None:
            items[items_id].id_package = update_dict['id_package']

        
        item = items[items_id]
        itemsOut = ItemOut(
            id_item=item.id_item,
            nome=item.nome,
            descricao=item.descricao,
            id_package=item.id_package,
            status=item.status
        )

        return itemsOut


    return HTTPException(status_code=404, detail="Encomenda não encontrada")


@router.get("/items/{items_id}/status")
async def update_items_status(items_id: int):
    if items_id in items:

        items[items_id].status = not items[items_id].status

        item = items[items_id]
        itemsOut = ItemOut(
            id_item=item.id_item,
            nome=item.nome,
            descricao=item.descricao,
            id_package=item.id_package,
            status=item.status
        )

        return itemsOut
        

    return HTTPException(status_code=404, detail="Encomenda não encontrada")


@router.delete("/items/{items_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_items(items_id: int):
    if items_id in items:

        del items[items_id]
        
        return {'message': 'Encomenda Deletada com Sucesso'}

    return HTTPException(status_code=404, detail="Encomenda não encontrada")