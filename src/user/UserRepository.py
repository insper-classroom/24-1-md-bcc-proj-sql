from sqlalchemy.orm import Session
from fastapi import HTTPException

from .User import User
from .UserDTO import UserIn, UserOut, UserUpdateSenha
from typing import List

class UserRepository:
    def get(db: Session, id_user: int) -> UserOut:
        user = db.query(User).filter(User.id_user == id_user).first()
        if user:
            return user.to_userOut()
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    
    def get_all(db: Session) -> List[UserOut]:
        users = db.query(User).all()
        return list(map(lambda user: user.to_userOut(), users))
    
    def create(db: Session, userIn: UserIn) -> UserOut:
        userIn.senha = UserRepository.hash_passord(userIn.senha, userIn.nome)
        user = User(**userIn.model_dump())
        db.add(user)
        db.commit()
        db.refresh(user)
        return user.to_userOut()
    
    def update(db: Session, id_user: int, new: UserUpdateSenha) -> UserOut:
        user = db.query(User).filter(User.id_user == id_user).first()
        if not user:
            raise HTTPException(status_code=404, detail="Usuário não encontrado")
        new.senha_antiga = UserRepository.hash_passord(new.senha_antiga, user.nome)
        if user.senha != new.senha_antiga:
            raise HTTPException(status_code=404, detail="Senha Atual Incorreta")
        user.senha = UserRepository.hash_passord(new.senha, user.nome)
        db.commit()
        return user.to_userOut()
    
    def update_status(db: Session, id_user: int):
        user = db.query(User).filter(User.id_user == id_user).first()
        if not user:
            raise HTTPException(status_code=404, detail="Usuário não encontrado")
        user.status = not user.status
        db.commit()
        return user.to_userOut()
    
    def delete(db: Session, id_user: int):
        rows_deleted = db.query(User).filter(User.id_user == id_user).delete()
        db.commit()
        if rows_deleted == 0:
            raise HTTPException(status_code=404, detail="Usuário não encontrado")
    
    def hash_passord(password: str, name: str) -> str:
        return str(hash(password + name))