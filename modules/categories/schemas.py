from pydantic import BaseModel, ConfigDict
from typing import Optional

class CategoriaCreateSchema(BaseModel):
    nombre: str

    model_config = ConfigDict(extra="ignore")

class CategoriaUpdateSchema(BaseModel):
    nombre: Optional[str]

    model_config = ConfigDict(extra="ignore")
