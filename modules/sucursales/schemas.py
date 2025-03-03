from pydantic import BaseModel, EmailStr, ConfigDict
from typing import Optional

class SucursalCreateSchema(BaseModel):
    nombre_sucursal: str
    numero_sucursal: str
    capacidad: int
    direccion: str
    telefono: str

    model_config = ConfigDict(extra="ignore")

class SucursalUpdateSchema(BaseModel):
    nombre_sucursal: Optional[str] = None
    numero_sucursal: Optional[str] = None
    capacidad: Optional[int] = None
    direccion: Optional[str] = None
    telefono: Optional[str] = None

    model_config = ConfigDict(extra="ignore")