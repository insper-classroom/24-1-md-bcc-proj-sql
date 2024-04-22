from fastapi import APIRouter, HTTPException, status

from typing import List, Dict

from models.user.user import User
from models.user.user_in import UserIn
from models.user.user_out import UserOut
from models.user.user_update import UserUpdateSenha

from db import DB

router = APIRouter()

@router.get("/accounts/", response_model=Dict[int, User])
def list_account():
    return DB.users.values()

@router.post("/accounts/", response_model=UserOut, status_code=status.HTTP_201_CREATED)
async def create_iaccount(userIn: UserIn):
    user_dict = userIn.model_dump()

    user_dict['id_user'] = len(DB.users)
    user_dict['senha'] = str(hash(user_dict['senha'] + user_dict['nome']))
    user = User(**user_dict)
    DB.users[user.id_user] = user

    userOut = UserOut(
        id_user=user.id_user,
        nome=user.nome,
        sobrenome=user.sobrenome,
        email=user.email,
        data_criacao=user.data_criacao,
        status=user.status
    )

    return userOut


@router.get("/accounts/{user_id}", response_model=UserOut)
def get_account(user_id: int):
    if user_id in DB.users:
        return DB.users[user_id]
    return HTTPException(status_code=404, detail="Usuário não encontrado")


@router.put("/accounts/{user_id}")
async def update_account(user_id: int, update: UserUpdateSenha):
    update_dict = update.model_dump()
    if user_id in DB.users:

        if str(hash(update_dict['senha'] + DB.users[user_id].nome)) == DB.users[user_id].senha:
            DB.users[user_id].senha = str(hash(update_dict['senha_nova'] + DB.users[user_id].nome))
        
            return DB.users[user_id]
        
        return HTTPException(status_code=404, detail="Senha Atual Incorreta")


    return HTTPException(status_code=404, detail="Usuário não encontrado")


@router.get("/accounts/{user_id}/status")
async def update_account_status(user_id: int):
    if user_id in DB.users:

        DB.users[user_id].status = not DB.users[user_id].status
        
        return DB.users[user_id]

    return HTTPException(status_code=404, detail="Usuário não encontrado")


@router.delete("/accounts/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_account(user_id: int):
    if user_id in DB.users:

        del DB.users[user_id]
        
        return {'message': 'Usuário Deletado com Sucesso'}

    return HTTPException(status_code=404, detail="Usuário não encontrado")