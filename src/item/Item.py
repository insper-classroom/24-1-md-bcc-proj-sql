from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime
from .ItemDTO import ItemOut

from database import Base
from datetime import datetime

class Item(Base):
    __tablename__ = "items"

    id_item =  Column(Integer, primary_key=True, index=True)
    nome = Column(String)
    data_criacao = Column(DateTime, default=datetime.now()) 
    descricao = Column(String)
    # id_package = Column(Integer, ForeignKey("packages.id_package"))
    id_package = Column(Integer)
    status = Column(Boolean, default=True)

    def to_itemOut(self) -> ItemOut:
        return ItemOut(
            id_item=self.id_item,
            nome=self.nome,
            descricao=self.descricao,
            id_package=self.id_package,
            status=self.status
        )
