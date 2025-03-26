# modules/ventas/services.py
from modules.generic.service_generic import BaseService
from modules.ventas.repositories import VentaRepository
from modules.ventas.schemas import VentaCreateSchema, VentaUpdateSchema
from database.db import db  # Importa db
from modules.detalleVenta.model import DetalleVenta # Importa DetalleVenta
from decimal import Decimal

class VentaService(BaseService):
    def __init__(self):
        super().__init__(VentaRepository(), VentaCreateSchema, VentaUpdateSchema)

    def create(self, data):
        # Validar los datos
        validated_data = self.create_schema(**data).model_dump()
        # Crear la venta
        nueva_venta = self.repository.model(**validated_data)
        nueva_venta.fecha_venta = validated_data['fecha_venta']
        # Calcular el total en el servicio
        total_venta = Decimal('0.00')  # Inicializar el total
        for linea_data in validated_data['lineas_producto']:
            precio_unitario = linea_data['precio_unitario']
            cantidad = linea_data['cantidad']
            descuento = linea_data['descuento']
            # Calcular el precio de la línea de producto
            subtotal = precio_unitario * cantidad
            descuento_aplicado = subtotal * (descuento / 100)
            total_linea = subtotal - descuento_aplicado
            total_venta += total_linea

        nueva_venta.total = total_venta  # Asignar el total calculado
        # Crear las líneas de producto
        for linea_data in validated_data['lineas_producto']:
            nueva_linea = DetalleVenta(  # Cambio:  DetalleVenta
                producto_id=linea_data['producto_id'],
                cantidad=linea_data['cantidad'],
                precio_unitario=linea_data['precio_unitario'],
                descuento=linea_data['descuento'],
                venta_id = nueva_venta.id # Asignar el venta_id
            )
            nueva_venta.detalles_venta.append(nueva_linea)  # Cambio: detalles_venta
        # Guardar en la base de datos
        try:
            self.repository.create(nueva_venta)
            return nueva_venta
        except Exception as e:
            db.session.rollback() # Rollback en caso de error
            raise e # Re-lanzar la excepción para que se propague
        return nueva_venta