from pydantic import BaseModel, ConfigDict
from typing import Optional
from datetime import datetime

class FacturaCreateSchema(BaseModel):
    venta_id: int
    metodo_pago_id: int
    fecha: Optional[datetime]

    model_config = ConfigDict(extra="ignore")

class FacturaUpdateSchema(BaseModel):
    venta_id: Optional[int]
    metodo_pago_id: Optional[int]
    fecha: Optional[datetime]

    model_config = ConfigDict(extra="ignore")
