from fastapi import APIRouter, HTTPException, status # type: ignore

from typing import List
from .TrackingDTO import Tracking, TrackingIn, TrackingUpdate
from .TrackingRepository import TrackingRepository
from src.package.PackageRepository import PackageRepository
from database import get_db

router = APIRouter()
db = get_db()

@router.get("/tracking", response_model=List[Tracking], tags=["tracking"])
def get_tracking(id_package: int = None, id_tracking: int = None): 
    """Returns a Specific Tracking based on the id for the move and the Package id"""
    if id_tracking:
        return [TrackingRepository.get(db,id_tracking)]
    if id_package:
        return TrackingRepository.get_by_package(db,id_package)
    else:
        return TrackingRepository.get_all(db)
    
@router.post("/tracking", response_model=Tracking, status_code=status.HTTP_201_CREATED, tags=["tracking"])
def new_tracking(movIn : TrackingIn):
    """Creates a New Tracking"""
    if(PackageRepository.existsById(db, movIn.id_package)):
        return TrackingRepository.create(db,movIn)
    raise HTTPException(status_code=404, detail="Encomenda não encontrada")

@router.put("/tracking/{id_tracking}", response_model=Tracking, tags=["tracking"])
def atualiza_tracking(id_tracking: int, movUpdate: TrackingUpdate):
    """Updates a Tracking's Status (where the package is in relation to the delivery pipeline)"""
    return TrackingRepository.update(db,id_tracking, movUpdate)

@router.delete("/tracking/{id_tracking}", status_code=status.HTTP_204_NO_CONTENT, tags=["tracking"])
def deleta_tracking(id_tracking: int):
    """Deletes a Tracking's information"""
    return TrackingRepository.delete(db,id_tracking)