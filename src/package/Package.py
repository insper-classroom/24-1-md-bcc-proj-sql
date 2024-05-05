from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime
from .PackageDTO import PackageOut

from database import Base
from datetime import datetime


class Package(Base):

    __tablename__ = "packages"

    id_package =  Column(Integer, primary_key=True, index=True)
    id_user = Column(Integer, ForeignKey("users.id_user"))
    data_criacao = Column(DateTime, default=datetime.now()) 
    status = Column(Boolean, default=True)

    def to_packageOut(self) -> PackageOut:
        return PackageOut(
            id_package=self.id_package,
            data_criacao=self.data_criacao,
            id_user=self.id_user,
            status=self.status
        )

