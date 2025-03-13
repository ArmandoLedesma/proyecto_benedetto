from database.db import db

class Producto(db.Model):
    __tablename__ = 'productos'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    image = db.Column(db.String(255), nullable=True)
    description = db.Column(db.String(255), nullable=False)
    precio = db.Column(db.Numeric(10,2), nullable=False)
    categoria_id = db.Column(db.Integer, db.ForeignKey('categorias.id'), nullable=False)
    # Se indica que esta relación se vincula con la propiedad 'productos' de Categoria.
    categoria = db.relationship('Categoria', back_populates='productos')
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
            'categoria_title': self.categoria.title if self.categoria else None,
            'is_active': self.is_active,
            'is_deleted': self.is_deleted
        }
