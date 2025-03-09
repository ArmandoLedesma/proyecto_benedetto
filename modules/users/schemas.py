from pydantic import BaseModel, EmailStr, ConfigDict
from typing import Optional

class UsuarioCreateSchema(BaseModel):
    id: int
    nombre: str
    email: EmailStr
    password: str
    rol: str = "cliente"
    estado: str = "Activo"

    model_config = ConfigDict(extra="ignore")

class UsuarioUpdateSchema(BaseModel):
    nombre: Optional[str]
    email: Optional[EmailStr]
    password: Optional[str]
    rol: Optional[str]
    estado: Optional[str]

    model_config = ConfigDict(extra="ignore")