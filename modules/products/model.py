from database.db import db
    
    
class Producto(db.Model):
    __tablename__ = 'productos'
    # Atributos
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    image = db.Column(db.String(255), nullable=True)  # Nuevo campo para la imagen
    description = db.Column(db.String(255), nullable=False)
    
    precio = db.Column(db.Numeric(10,2), nullable=False)

    # Clave foránea que relaciona Producto con Categoria
    categoria_id = db.Column(db.Integer, db.ForeignKey('categorias.id'), nullable=False)
    # Estados
    is_active = db.Column(db.Boolean, nullable=False, default=True)
    is_deleted = db.Column(db.Boolean, nullable=False, default=False)

    def to_dict(self):  
        return {
            'id': self.id,
            'nombre': self.nombre,
            'image': self.image,
            'description': self.description,
            'precio': self.precio,
            'categoria_id': self.categoria_id,
            'is_active': self.is_active,
            'is_deleted': self.is_deleted
        }