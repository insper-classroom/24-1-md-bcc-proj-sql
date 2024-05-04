from fastapi import APIRouter, HTTPException, status

from typing import List
from .PackageDTO import PackageIn, PackageOut
from .PackageRepository import PackageRepository
from database import get_db

router = APIRouter()
db = get_db()

@router.get("/packages/{package_id}", response_model=PackageOut, tags=["packages"])
def get(package_id: int):
    """Returns an Package's information based on the id given"""
    return PackageRepository.get(db, package_id)

@router.get("/packages/", response_model=List[PackageOut], tags=["packages"])
def get_all():
    """Lists all packages"""
    return PackageRepository.get_all(db)

@router.post("/packages/", response_model=PackageOut, status_code=status.HTTP_201_CREATED, tags=["packages"])
def post(packageIn: PackageIn):
    """Creates a New package"""
    return PackageRepository.create(db, packageIn)

@router.put("/packages/{package_id}/status", response_model=PackageOut, tags=["packages"])
def update_status(package_id: int):
    """Updates an Package's Status (Available or Not)"""
    return PackageRepository.update_status(db, package_id)

@router.delete("/packages/{package_id}", status_code=status.HTTP_204_NO_CONTENT, tags=["packages"])
def delete(package_id: int):
    """Deletes a Package's information"""
    return PackageRepository.delete(db, package_id)