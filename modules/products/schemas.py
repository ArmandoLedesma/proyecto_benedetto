from pydantic import BaseModel, ConfigDict
from typing import Optional

class ProductoCreateSchema(BaseModel):
    nombre: str
    description: str
    precio: float
    categoria_id: int
    is_active: Optional[bool] = True
    is_deleted: Optional[bool] = False

    model_config = ConfigDict(extra="ignore")

class ProductoUpdateSchema(BaseModel):
    nombre: Optional[str] = None
    description: Optional[str] = None
    precio: Optional[float] = None
    categoria_id: Optional[int] = None
    is_active: Optional[bool] = None
    is_deleted: Optional[bool] = None

    model_config = ConfigDict(extra="ignore")
