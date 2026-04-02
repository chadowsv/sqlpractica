from fastapi import APIRouter, HTTPException
from sqlmodel import select
from db import SessionDep
from models.book import Book   # IMPORTANTE

books = APIRouter(prefix="/books", tags=["books"])

@books.post("/")
def create_book(book: Book, session: SessionDep):
    session.add(book)
    session.commit()
    session.refresh(book)
    return book

@books.get("/")
def listar_libros(session: SessionDep):
    libros = session.exec(select(Book)).all()
    return libros

@books.get("/{book_id}")
def obtener_libro(book_id: int, session: SessionDep):
    book = session.get(Book, book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Libro no encontrado")
    return book

@books.delete("/{book_id}")
def eliminar_libro(book_id: int, session: SessionDep):
    book = session.get(Book, book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Libro no encontrado")
    session.delete(book)
    session.commit()
    return {"ok": True}