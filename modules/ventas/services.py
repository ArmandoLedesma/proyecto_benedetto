from modules.generic.service_generic import BaseService
from modules.ventas.repositories import VentaRepository
from modules.ventas.schemas import VentaCreateSchema, VentaUpdateSchema
from modules.detalleVenta.schemas import DetalleVentaCreateSchema
from modules.ventas.model import Venta
from modules.detalleVenta.model import DetalleVenta
from database.db import db
from decimal import Decimal
from datetime import date

class VentaService(BaseService):
    def __init__(self):
        super().__init__(VentaRepository(), VentaCreateSchema, VentaUpdateSchema)
        self.schema_create = VentaCreateSchema
        self.schema_update = VentaUpdateSchema

    def create(self, data):
        # Validar los datos con el schema
        validated_data = self.schema_create(**data).model_dump()

        # Separar las líneas de producto de los datos de la venta
        lineas_producto_data = validated_data.pop('lineas_producto', [])

        # Crear la venta
        nueva_venta = Venta(
            fecha_venta=validated_data.get('fecha_venta'),
            empleado_id=validated_data.get('empleado_id'),
            cliente_id=validated_data.get('cliente_id'),
            sucursal_id=validated_data.get('sucursal_id'),
            metodo_pago_id=validated_data.get('metodo_pago_id'),
            total=validated_data.get('total'),
            detalles=validated_data.get('detalles')
        )

        # Agregar la venta a la sesión
        db.session.add(nueva_venta)

        # Hacer commit de la transacción PARA OBTENER EL ID DE LA VENTA
        db.session.flush()  # Usamos flush en lugar de commit

        # Crear los detalles de venta y asociarlos a la venta
        for linea_producto_data in lineas_producto_data:
            detalle_venta = DetalleVenta(
                venta_id=nueva_venta.id,
                producto_id=linea_producto_data.get('producto_id'),
                cantidad=linea_producto_data.get('cantidad'),
                precio_unitario=linea_producto_data.get('precio_unitario'),
                descuento=linea_producto_data.get('descuento')
            )
            db.session.add(detalle_venta)

        # Hacer commit de la transacción para guardar los detalles de venta
        db.session.commit()

        # Recargar la venta para obtener los detalles de venta
        db.session.refresh(nueva_venta)

        return nueva_venta