from pydantic import BaseModel, ConfigDict
from typing import List, Optional
from datetime import date
from decimal import Decimal

class DetalleVentaCreateSchema(BaseModel):  # Renombrar la clase
    producto_id: int
    cantidad: int
    precio_unitario: Decimal
    descuento: Optional[Decimal] = 0

    model_config = ConfigDict(extra="ignore")

class VentaCreateSchema(BaseModel):
    fecha_venta: date
    empleado_id: int
    cliente_id: int
    sucursal_id: int
    metodo_pago_id: int
    total: Decimal
    detalles: Optional[str] = None
    lineas_producto: List[DetalleVentaCreateSchema]  # Cambio: ahora usa DetalleVentaCreateSchema

    model_config = ConfigDict(extra="ignore")

class VentaUpdateSchema(BaseModel):
    fecha_venta: Optional[date] = None
    empleado_id: Optional[int] = None
    cliente_id: Optional[int] = None
    sucursal_id: Optional[int] = None
    metodo_pago_id: Optional[int] = None
    total: Optional[Decimal] = None
    detalles: Optional[str] = None

    model_config = ConfigDict(extra="ignore")