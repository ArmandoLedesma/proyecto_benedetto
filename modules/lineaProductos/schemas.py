from pydantic import BaseModel, ConfigDict
from typing import Optional

class LineaProductoCreateSchema(BaseModel):
    sucursal_id: int
    producto_id: int
    stock: int

    model_config = ConfigDict(extra="ignore")

class LineaProductoUpdateSchema(BaseModel):
    sucursal_id: Optional[int]
    producto_id: Optional[int]
    stock: Optional[int]

    model_config = ConfigDict(extra="ignore")
