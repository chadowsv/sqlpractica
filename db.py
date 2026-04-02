from sqlmodel import SQLModel, Session, create_engine
from fastapi import FastAPI
from typing import Annotated
from fastapi import Depends
import os
from dotenv import load_dotenv
load_dotenv()
#Conexion a la bdd
DATABASE_URL = os.getenv("DATABASE_URL")
if not DATABASE_URL:
    raise ValueError("DATABASE_URL no está definida en el .env")
engine = create_engine(DATABASE_URL,echo=True)

def create_all_tables(app: FastAPI):
    SQLModel.metadata.create_all(engine)
    #Pasa y luego continua con la ejecución de la aplicación
    yield
def get_session():
    with Session(engine) as session:
        yield session
#Depends significa que se va a encargar automaticamente de crear una sesión y pasarla a la función que lo requiera
SessionDep = Annotated[Session, Depends(get_session)]