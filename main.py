# run: uvicorn main:app --reload

from fastapi import FastAPI # type: ignore
from typing import List
from routes import movimentacao, packages, accounts, items

app = FastAPI()
app.include_router(movimentacao.router)
app.include_router(packages.router)
app.include_router(accounts.router)
app.include_router(items.router)

@app.get("/")
def root():
    return {"Hello": "World"}