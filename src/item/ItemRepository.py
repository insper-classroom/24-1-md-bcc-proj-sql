from sqlalchemy.orm import Session
from fastapi import HTTPException

from .Item import Item
from .ItemDTO import ItemIn, ItemOut, ItemUpdate
from typing import List

class ItemRepository:
    def get_item(db: Session, id_item: int) -> ItemOut:
        item = db.query(Item).filter(Item.id_item == id_item).first()
        if item:
            return item.to_itemOut()
        raise HTTPException(status_code=404, detail="Item da encomenda não encontrada")
    
    def get_items(db: Session) -> List[ItemOut]:
        items = db.query(Item).all()
        return list(map(lambda item: item.to_itemOut(), items))
    
    def create_item(db: Session, item: ItemIn) -> ItemOut:
        item = Item(**item.model_dump())
        db.add(item)
        db.commit()
        db.refresh(item)
        return item.to_itemOut()
    
    def update_item(db: Session, id_item: int, new: ItemUpdate) -> ItemOut:
        rows_affected = db.query(Item).filter(Item.id_item == id_item).update(new.model_dump(exclude_unset=True))
        db.commit()
        if rows_affected == 0:
            raise HTTPException(status_code=404, detail="Item da encomenda não encontrada")
        return ItemRepository.get_item(db, id_item)
    
    def update_item_status(db: Session, id_item: int):
        item = db.query(Item).filter(Item.id_item == id_item).first()
        if not item:
            raise HTTPException(status_code=404, detail="Item da encomenda não encontrada")
        item.status = not item.status
        db.commit()
        return item.to_itemOut()
    
    def delete_item(db: Session, id_item: int):
        rows_deleted = db.query(Item).filter(Item.id_item == id_item).delete()
        db.commit()
        if rows_deleted == 0:
            raise HTTPException(status_code=404, detail="Item da encomenda não encontrada")