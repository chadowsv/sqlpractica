from fastapi import APIRouter, HTTPException
from sqlmodel import select
from db import SessionDep
from models.usuario import Usuario
users = APIRouter(prefix="/users", tags=["users"])

@users.post("/")
def create_user(usuario: Usuario, session: SessionDep):
    session.add(usuario)
    session.commit()
    session.refresh(usuario)
    return usuario
@users.get("/")
def listar_usuarios(session: SessionDep):
    usuarios = session.exec(select(Usuario)).all()
    return usuarios
@users.get("/{usuario_id}")
def obtener_usuario(usuario_id: int, session: SessionDep):
    usuario = session.get(Usuario, usuario_id)
    return usuario
@users.put("/{usuario_id}")
def actualizar_usuario(usuario_id: int, datos: Usuario, session: SessionDep):
    usuario = session.get(Usuario, usuario_id)

    if not usuario:
        return {"error": "No encontrado"}

    usuario.nombre = datos.nombre
    usuario.email = datos.email

    session.commit()
    session.refresh(usuario)

    return usuario
@users.delete("/{usuario_id}")
def eliminar_usuario(usuario_id: int, session: SessionDep):
    usuario = session.get(Usuario, usuario_id)
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    session.delete(usuario)
    session.commit()
    return{"ok":True}