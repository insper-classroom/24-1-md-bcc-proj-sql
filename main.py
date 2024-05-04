# run: uvicorn main:app --reload

from fastapi import FastAPI # type: ignore
from typing import List
from routes import movimentacao, packages, accounts, items
from src.item import ItemRoutes
from src.tracking import TrackingRoutes
from database import engine, Base

# Cria todas as tabelas no banco de dados
Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(TrackingRoutes.router)
app.include_router(packages.router)
app.include_router(accounts.router)
app.include_router(ItemRoutes.router)

@app.get("/")
def root():
    return {"Hello": "World"}