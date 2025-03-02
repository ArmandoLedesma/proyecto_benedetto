from pydantic import BaseModel, EmailStr, ConfigDict
from typing import Optional

class ClienteCreateSchema(BaseModel):
    nombre: str
    telefono: str
    email: EmailStr
    estado: Optional[str] = "Activo"
    
    model_config = ConfigDict(extra="ignore")

class ClienteUpdateSchema(BaseModel):
    nombre: Optional[str] = None
    telefono: Optional[str] = None
    email: Optional[EmailStr] = None
    estado: Optional[str] = None

    model_config = ConfigDict(extra="ignore")