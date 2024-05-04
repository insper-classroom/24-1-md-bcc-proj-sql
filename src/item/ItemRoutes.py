from fastapi import APIRouter, HTTPException, status

from typing import List
from .ItemDTO import ItemIn, ItemOut, ItemUpdate
from .ItemRepository import ItemRepository
from database import get_db

router = APIRouter()
db = get_db()

@router.get("/items/{item_id}", response_model=ItemOut, tags=["items"])
def get(item_id: int):
    """Returns an Item's information based on the id given"""
    return ItemRepository.get(db, item_id)

@router.get("/items/", response_model=List[ItemOut], tags=["items"])
def get_all():
    """Lists all Items"""
    return ItemRepository.get_all(db)

@router.get("/items/package/{package_id}", response_model=List[ItemOut], tags=["items"])
def get_all_from_package(package_id: int):
    """Returns a list of Items in a Package based on the Package's id given"""
    return ItemRepository.get_all_from_package(db, package_id)

@router.post("/items/", response_model=ItemOut, status_code=status.HTTP_201_CREATED, tags=["items"])
def post(itemIn: ItemIn):
    """Creates a New Item"""
    # verificar em package_repository a existencia desse package
    # if itemIn.id_package:
    #     DB.checkPackage(itemIn.id_package)
    return ItemRepository.create(db, itemIn)

@router.put("/items/{item_id}", response_model=ItemOut, tags=["items"])
def update(item_id: int, item_update: ItemUpdate):
    """Updates an Item's information"""
    return ItemRepository.update(db, item_id, item_update)

@router.put("/items/{item_id}/status", response_model=ItemOut, tags=["items"])
def update_status(item_id: int):
    """Updates an Item's Status (Available or Not)"""
    return ItemRepository.update_status(db, item_id)

@router.delete("/items/{item_id}", status_code=status.HTTP_204_NO_CONTENT, tags=["items"])
def delete(item_id: int):
    """Deletes a Package's information"""
    return ItemRepository.delete(db, item_id)