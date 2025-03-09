from pydantic import BaseModel, ConfigDict
from typing import Optional

class VentaCreateSchema(BaseModel):
    empleado_id: int
    producto_id: int
    cantidad: int

    model_config = ConfigDict(extra="ignore")

class VentaUpdateSchema(BaseModel):
    empleado_id: Optional[int]
    producto_id: Optional[int]
    cantidad: Optional[int]

    model_config = ConfigDict(extra="ignore")
