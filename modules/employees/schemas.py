from pydantic import BaseModel, EmailStr, ConfigDict
from decimal import Decimal
from typing import Optional

class EmpleadoCreateSchema(BaseModel):
    id : str
    nombre: str
    cargo: str
    salario: Decimal
    telefono: str
    email: EmailStr

    model_config = ConfigDict(extra="ignore")

class EmpleadoUpdateSchema(BaseModel):
    nombre: Optional[str] = None
    cargo: Optional[str] = None
    salario: Optional[Decimal] = None
    telefono: Optional[str] = None
    email: Optional[EmailStr] = None

    model_config = ConfigDict(extra="ignore")