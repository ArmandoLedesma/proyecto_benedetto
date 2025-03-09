from pydantic import BaseModel, ConfigDict
from typing import Optional

class PedidoCreateSchema(BaseModel):
    cliente_id: int
    producto_id: int
    estado: Optional[str] = "Pendiente"

    model_config = ConfigDict(extra="ignore")

class PedidoUpdateSchema(BaseModel):
    cliente_id: Optional[int]
    producto_id: Optional[int]
    estado: Optional[str]

    model_config = ConfigDict(extra="ignore")
