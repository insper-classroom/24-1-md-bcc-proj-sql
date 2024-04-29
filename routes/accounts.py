from fastapi import APIRouter, HTTPException, status

from typing import List

from models.user.user import User
from models.user.user_in import UserIn
from models.user.user_out import UserOut
from models.user.user_update import UserUpdateSenha

from db import DB

router = APIRouter()

@router.get("/accounts/", response_model=List[UserOut], tags=["accounts"])
def list_account():
    """Lists all Accounts"""
    return DB.getUsers()

@router.post("/accounts/", response_model=UserOut, status_code=status.HTTP_201_CREATED, tags=["accounts"])
def create_account(userIn: UserIn):
    """Creates a New Account"""
    user_dict = userIn.model_dump()

    user_dict['id_user'] = DB.usersNextID
    DB.usersIncID() 
    user_dict['senha'] = str(hash(user_dict['senha'] + user_dict['nome']))
    user = User(**user_dict)
    DB.users[user.id_user] = user

    return DB.getUser(user.id_user)

@router.get("/accounts/{user_id}", response_model=UserOut, tags=["accounts"])
def get_account(user_id: int):
    """Returns an Account given its id"""
    if user_id in DB.users:
        return DB.getUser(user_id)
    raise HTTPException(status_code=404, detail="Usuário não encontrado")

@router.put("/accounts/{user_id}", response_model=UserOut, tags=["accounts"])
def update_account(user_id: int, update: UserUpdateSenha):
    """Updates an Accounts's information"""
    update_dict = update.model_dump()
    if user_id in DB.users:
        if str(hash(update_dict['senha'] + DB.users[user_id].nome)) == DB.users[user_id].senha:
            DB.users[user_id].senha = str(hash(update_dict['senha_nova'] + DB.users[user_id].nome))
            return DB.getUser(user_id)
        raise HTTPException(status_code=404, detail="Senha Atual Incorreta")
    raise HTTPException(status_code=404, detail="Usuário não encontrado")

@router.put("/accounts/{user_id}/status", response_model=UserOut, tags=["accounts"])
def update_account_status(user_id: int):
    """Updates an Account's Status (in use or deactivated)"""
    if user_id in DB.users:
        DB.users[user_id].status = not DB.users[user_id].status
        return DB.getUser(user_id)
    raise HTTPException(status_code=404, detail="Usuário não encontrado")

@router.delete("/accounts/{user_id}", status_code=status.HTTP_204_NO_CONTENT, tags=["accounts"])
def delete_account(user_id: int):
    """Deletes an Account's information"""
    if user_id in DB.users:
        del DB.users[user_id]
        return {'message': 'Usuário Deletado com Sucesso'}
    raise HTTPException(status_code=404, detail="Usuário não encontrado")