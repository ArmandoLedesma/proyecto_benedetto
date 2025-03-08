from pydantic import BaseModel, ConfigDict
from typing import Optional

class MetodoPagoCreateSchema(BaseModel):
    nombre: str

    model_config = ConfigDict(extra="ignore")

class MetodoPagoUpdateSchema(BaseModel):
    nombre: Optional[str]

    model_config = ConfigDict(extra="ignore")
