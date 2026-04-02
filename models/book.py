from sqlmodel import SQLModel, Field
from typing import Optional
class Book(SQLModel, table=True):
    id:Optional[int] = Field(default=None, primary_key=True)
    titulo:str
    autor:str