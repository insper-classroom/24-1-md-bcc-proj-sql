from fastapi import APIRouter, HTTPException, status

from typing import List, Dict

from Classes.user.user import User
from Classes.user.user_in import UserIn
from Classes.user.user_out import UserOut
from Classes.user.user_update import UserUpdateSenha


router = APIRouter()

users = {}

@router.get("/accounts/", response_model=Dict[int, User])
def list_account():
    return users


@router.post("/accounts/", response_model=UserOut, status_code=status.HTTP_201_CREATED)
async def create_iaccount(userIn: UserIn):
    user_dict = userIn.model_dump()

    user_dict['id_user'] = len(users)
    user_dict['senha'] = str(hash(user_dict['senha'] + user_dict['nome']))
    user = User(**user_dict)
    users[user.id_user] = user

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
    if user_id in users:
        return users[user_id]
    return HTTPException(status_code=404, detail="Usuário não encontrado")


@router.put("/accounts/{user_id}")
async def update_account(user_id: int, update: UserUpdateSenha):
    update_dict = update.model_dump()
    if user_id in users:

        if str(hash(update_dict['senha'] + users[user_id].nome)) == users[user_id].senha:
            users[user_id].senha = str(hash(update_dict['senha_nova'] + users[user_id].nome))
        
            return users[user_id]
        
        return HTTPException(status_code=404, detail="Senha Atual Incorreta")


    return HTTPException(status_code=404, detail="Usuário não encontrado")


@router.get("/accounts/{user_id}/status")
async def update_account_status(user_id: int):
    if user_id in users:

        users[user_id].status = not users[user_id].status
        
        return users[user_id]

    return HTTPException(status_code=404, detail="Usuário não encontrado")


@router.delete("/accounts/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_account(user_id: int):
    if user_id in users:

        del users[user_id]
        
        return {'message': 'Usuário Deletado com Sucesso'}

    return HTTPException(status_code=404, detail="Usuário não encontrado")