from sqlalchemy.orm import Session

from .ItemModel import Item
from .ItemSchemas import ItemIn, ItemOut, ItemUpdate
from typing import List

def get_item(db: Session, item_id: int) -> ItemOut:
    item = db.query(Item).filter(Item.id == item_id).first()
    return ItemOut(**item.model_dump())

def get_items(db: Session) -> List[ItemOut]:
    items = db.query(Item).all()
    return list(map(lambda item: ItemOut(**item.model_dump()), items))

def create_item(db: Session, item: ItemIn) -> ItemOut:
    item = Item(**item.model_dump())
    db.add(item)
    db.commit()
    db.refresh(item)
    return ItemOut(**item.model_dump())

def update_item(db: Session, item_id: int, new: ItemUpdate) -> ItemOut:
    item = db.query(Item).filter(Item.id == item_id).update(new)
    db.commit()
    return ItemOut(**item.model_dump())

def delete_item(db: Session, item_id: int):
    db.query(Item).filter(Item.id == item_id).delete()
    db.commit()