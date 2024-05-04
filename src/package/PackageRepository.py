from sqlalchemy.orm import Session
from fastapi import HTTPException

from .Package import Package
from .PackageDTO import PackageIn, PackageOut
from typing import List

class PackageRepository:
    def get(db: Session, id_package: int) -> PackageOut:
        package = db.query(Package).filter(Package.id_package == id_package).first()
        if package:
            return package.to_packageOut()
        raise HTTPException(status_code=404, detail="Encomenda não encontrada")
    
    def get_all(db: Session) -> List[PackageOut]:
        packages = db.query(Package).all()
        return list(map(lambda package: package.to_PackageOut(), packages))
    
    def create(db: Session, package: PackageIn) -> PackageOut:
        package = Package(**package.model_dump())
        db.add(package)
        db.commit()
        db.refresh(package)
        return package.to_packageOut()
    
    def update_status(db: Session, id_package: int):
        package = db.query(Package).filter(Package.id_package == id_package).first()
        if not package:
            raise HTTPException(status_code=404, detail="Encomenda não encontrada")
        package.status = not package.status
        db.commit()
        return package.to_packageOut()
    
    def delete(db: Session, id_package: int):
        rows_deleted = db.query(Package).filter(Package.id_package == id_package).delete()
        db.commit()
        if rows_deleted == 0:
            raise HTTPException(status_code=404, detail="Encomenda não encontrada")