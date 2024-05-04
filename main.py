# run: uvicorn main:app --reload

from fastapi import FastAPI # type: ignore
from typing import List
from routes import movimentacao, packages, accounts, items
from item import ItemRouter
from database import engine, Base

# Cria todas as tabelas no banco de dados
Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(movimentacao.router)
app.include_router(packages.router)
app.include_router(accounts.router)
app.include_router(ItemRouter.router)

@app.get("/")
def root():
    return {"Hello": "World"}