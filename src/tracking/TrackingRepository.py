from sqlalchemy.orm import Session
from fastapi import HTTPException

from .Tracking import Tracking
from .TrackingDTO import TrackingIn, TrackingUpdate
from typing import List

class TrackingRepository:
    def get(db: Session, id_tracking: int) -> Tracking:
        tracking = db.query(Tracking).filter(Tracking.id_tracking == id_tracking).first()
        if tracking:
            return tracking
        raise HTTPException(status_code=404, detail="Tracking não encontrada")

    def get_all(db: Session) -> List[Tracking]:
        trackings = db.query(Tracking).all()
        return trackings
    
    def get_by_package(db: Session, id_package: int) -> List[Tracking]:
        trackings = db.query(Tracking).filter(Tracking.id_package == id_package).all()
        if len(trackings) == 0:
            raise HTTPException(status_code=404, detail="Nenhuma movimentação encontrada para a encomenda informada")  
        return trackings

    def create(db: Session, tracking: TrackingIn) -> Tracking:
        tracking = Tracking(**tracking.model_dump())
        db.add(tracking)
        db.commit()
        db.refresh(tracking)
        return tracking

    def update(db: Session, id_tracking: int, new: TrackingUpdate) -> Tracking:
        rows_affected = db.query(Tracking).filter(Tracking.id_tracking == id_tracking).update(new.model_dump())
        db.commit()
        if rows_affected == 0:
            raise HTTPException(status_code=404, detail="Tracking não encontrada")
        return TrackingRepository.get(db, id_tracking)

    def delete(db: Session, id_tracking: int):
        rows_deleted = db.query(Tracking).filter(Tracking.id_tracking == id_tracking).delete()
        db.commit()
        if rows_deleted == 0:
            raise HTTPException(status_code=404, detail="Tracking não encontrada")