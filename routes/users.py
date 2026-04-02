from fastapi import APIRouter, HTTPException
from sqlmodel import select
from db import SessionDep
from models.usuario import UserCreate, User
users = APIRouter(prefix="/users", tags=["users"])

@users.post("/")
def create_user(usuario: UserCreate, session: SessionDep):
    db_user = User(nombre=usuario.nombre, email=usuario.email)
    session.add(db_user)
    session.commit()
    session.refresh(db_user)
    return db_user
@users.get("/")
def listar_usuarios(session: SessionDep):
    usuarios = session.exec(select(User)).all()
    return usuarios
@users.get("/{usuario_id}")
def obtener_usuario(usuario_id: int, session: SessionDep):
    usuario = session.get(User, usuario_id)
    return usuario
@users.put("/{usuario_id}")
def actualizar_usuario(usuario_id: int, datos: User, session: SessionDep):
    usuario = session.get(User, usuario_id)

    if not usuario:
        return {"error": "No encontrado"}

    usuario.nombre = datos.nombre
    usuario.email = datos.email

    session.commit()
    session.refresh(usuario)

    return usuario
@users.delete("/{usuario_id}")
def eliminar_usuario(usuario_id: int, session: SessionDep):
    usuario = session.get(User, usuario_id)
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    session.delete(usuario)
    session.commit()
    return{"ok":True}