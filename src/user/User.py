from sqlalchemy import Boolean, Column, Integer, String, DateTime
from .UserDTO import UserOut

from database import Base
from datetime import datetime

class User(Base):

    __tablename__ = "users"

    id_user = Column(Integer, primary_key=True, index=True)
    nome = Column(String)
    sobrenome = Column(String)
    data_criacao = Column(DateTime, default=datetime.now()) 
    senha = Column(String)
    email = Column(String)
    status = Column(Boolean, default=True)

    def to_userOut(self) -> UserOut:
        return UserOut(
            id_user=self.id_user,
            nome=self.nome,
            sobrenome=self.sobrenome,
            email=self.email,
            status=self.status
        )
