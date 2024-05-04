from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship

from database import Base
from datetime import datetime

class Item(Base):
    __tablename__ = "items"

    id_item =  Column(Integer, primary_key=True, index=True)
    nome = Column(String)
    data_criacao = Column(DateTime, default=datetime.now()) 
    descricao = Column(String)
    id_package = Column(Integer, ForeignKey("packages.id_package"))
    status = Column(Boolean)

