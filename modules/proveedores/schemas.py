from pydantic import BaseModel, EmailStr, ConfigDict
from typing import Optional

class ProveedorCreateSchema(BaseModel):
    nombre: str
    contacto: str
    telefono: str
    email: EmailStr

    model_config = ConfigDict(extra="ignore")

class ProveedorUpdateSchema(BaseModel):
    nombre: Optional[str]
    contacto: Optional[str]
    telefono: Optional[str]
    email: Optional[EmailStr]

    model_config = ConfigDict(extra="ignore")
