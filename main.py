# run: uvicorn main:app --reload

from fastapi import FastAPI # type: ignore
from typing import List
from routes import movimentacao, localizacao, accounts

app = FastAPI()
app.include_router(movimentacao.router)
app.include_router(localizacao.router)
app.include_router(accounts.router)

@app.get("/")
def root():
    return {"Hello": "World"}