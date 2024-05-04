from sqlalchemy.orm import Session
from fastapi import HTTPException

from .User import User
from .UserDTO import UserIn, UserOut, UserUpdateSenha
from typing import List

class UserRepository:
    def get(db: Session, id_user: int) -> UserOut:
        user = db.query(User).filter(User.id_user == id_user).first()
        if user:
            return user.to_UserOut()
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    
    def get_all(db: Session) -> List[UserOut]:
        users = db.query(User).all()
        return list(map(lambda user: user.to_UserOut(), users))
    
    def create(db: Session, user: UserIn) -> UserOut:
        user = User(**user.model_dump())
        db.add(user)
        db.commit()
        db.refresh(user)
        return user.to_UserOut()
    
    def update(db: Session, id_user: int, new: UserUpdateSenha) -> UserOut:
        rows_affected = db.query(User).filter(User.id_user == id_user, User.senha == new.senha_antiga).update(new.model_dump(exclude_unset=True))
        db.commit()
        if rows_affected == 0:
            raise HTTPException(status_code=404, detail="Usuário não encontrado")
        return UserRepository.get(db, id_user)
    
    def update_status(db: Session, id_user: int):
        user = db.query(User).filter(User.id_user == id_user).first()
        if not user:
            raise HTTPException(status_code=404, detail="Usuário não encontrado")
        user.status = not user.status
        db.commit()
        return user.to_UserOut()
    
    def delete(db: Session, id_user: int):
        rows_deleted = db.query(User).filter(User.id_user == id_user).delete()
        db.commit()
        if rows_deleted == 0:
            raise HTTPException(status_code=404, detail="Usuário não encontrado")