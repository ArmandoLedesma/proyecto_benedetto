from pydantic import BaseModel, ConfigDict
from typing import Optional
from decimal import Decimal

class ProductoCreateSchema(BaseModel):
    nombre: str
    precio: Decimal
    categoria_id: int

    model_config = ConfigDict(extra="ignore")

class ProductoUpdateSchema(BaseModel):
    nombre: Optional[str]
    precio: Optional[Decimal]
    categoria_id: Optional[int]

    model_config = ConfigDict(extra="ignore")
