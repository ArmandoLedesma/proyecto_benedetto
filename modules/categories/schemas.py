from pydantic import BaseModel, ConfigDict
from typing import Optional


# ✅ Esquema para la creación de una categoría
class CategoriaCreateSchema(BaseModel):
    title: str
    description: str
    image: str
    button_text: str
    is_active: Optional[bool] = True
    is_deleted: Optional[bool] = False
    model_config = ConfigDict(from_attributes=True)

# ✅ Esquema para la actualización de una categoría (todos los campos opcionales)
class CategoriaUpdateSchema(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    image: Optional[str] = None
    button_text: Optional[str] = None
    is_active: Optional[bool] = None
    is_deleted: Optional[bool] = None
    model_config = ConfigDict(from_attributes=True)

# ✅ Esquema para la respuesta de una categoría
class CategoriaResponseSchema(BaseModel):
    id: int
    title: str
    description: str
    image: str
    button_text: str
    is_active: bool
    is_deleted: bool

    model_config = ConfigDict(from_attributes=True)

