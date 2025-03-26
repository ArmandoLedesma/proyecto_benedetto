from pydantic import BaseModel, ConfigDict
from typing import Optional

class MetodoPagoCreateSchema(BaseModel):
    nombre: str
    descripcion: Optional[str]
    

    model_config = ConfigDict(extra="ignore")

class MetodoPagoUpdateSchema(BaseModel):
    nombre: Optional[str]
    descripcion: Optional[str]
    
    model_config = ConfigDict(extra="ignore")
