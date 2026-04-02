from fastapi import FastAPI
from sqlmodel import select
from contextlib import asynccontextmanager
from db import create_all_tables, SessionDep
from routes.users import users
#Ejecucion de create_all_tables al iniciar la aplicacion
app = FastAPI(lifespan=create_all_tables)
app.include_router(users)

@app.get("/")
def read_root():
    return {"Hello": "World"}
@app.get("/check-db")
def checkdb(session: SessionDep):
    result = session.exec(select(1)).first()
    return {"Database Connection": result}