from fastapi import APIRouter, HTTPException, status

from typing import List
from .UserDTO import UserIn, UserOut, UserUpdateSenha
from .UserRepository import UserRepository
from database import get_db

router = APIRouter()
db = get_db()

@router.get("/users/{user_id}", response_model=UserOut, tags=["users"])
def get(user_id: int):
    """Returns an User's information based on the id given"""
    return UserRepository.get(db, user_id)

@router.get("/users/", response_model=List[UserOut], tags=["users"])
def get_all():
    """Lists all users"""
    return UserRepository.get_all(db)

@router.post("/users/", response_model=UserOut, status_code=status.HTTP_201_CREATED, tags=["users"])
def post(userIn: UserIn):
    """Creates a New User"""
    return UserRepository.create(db, userIn)

@router.put("/users/{user_id}", response_model=UserOut, tags=["users"])
def update(user_id: int, item_update: UserUpdateSenha):
    """Updates an User's information (password)"""
    return UserRepository.update(db, user_id, item_update)

@router.put("/users/{user_id}/status", response_model=UserOut, tags=["users"])
def update_status(user_id: int):
    """Updates an User's Status (Available or Not)"""
    return UserRepository.update_status(db, user_id)

@router.delete("/users/{user_id}", status_code=status.HTTP_204_NO_CONTENT, tags=["users"])
def delete(user_id: int):
    """Deletes a User's information"""
    return UserRepository.delete(db, user_id)