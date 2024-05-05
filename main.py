# run: uvicorn main:app --reload

from fastapi import FastAPI # type: ignore
from typing import List
from src.item import ItemRoutes
from src.tracking import TrackingRoutes
from src.package import PackageRoutes
from src.user import UserRoutes
from database import engine, Base

# Cria todas as tabelas no banco de dados
Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(TrackingRoutes.router)
app.include_router(PackageRoutes.router)
app.include_router(UserRoutes.router)
app.include_router(ItemRoutes.router)

@app.get("/")
def root():
    return {"Hello": "World"}