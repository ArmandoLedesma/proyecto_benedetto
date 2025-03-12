from database.db import db

class Categoria(db.Model):
    __tablename__ = 'categorias'
    # Atributos
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False, unique=True)
    description = db.Column(db.String(255), nullable=False)
    image = db.Column(db.String(255), nullable=False)
    button_text = db.Column(db.String(50), nullable=False)
    url = db.Column(db.String(200), nullable=False)
    # Estados
    is_active = db.Column(db.Boolean, nullable=False, default=1)
    is_deleted = db.Column(db.Boolean, nullable=False, default=0)
    # Relaciones
    productos = db.relationship('Producto', backref='categoria', lazy=True)

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'image': self.image,
            'button_text': self.button_text,
            'url': self.url,
            'is_active': self.is_active,
            'is_deleted': self.is_deleted
        }