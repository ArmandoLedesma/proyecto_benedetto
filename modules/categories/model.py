from database.db import db

class Categoria(db.Model):
    __tablename__ = 'categorias'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    image = db.Column(db.String(255), nullable=False)
    description = db.Column(db.String(255), nullable=False)
    button_text = db.Column(db.String(255), nullable=False)
    url = db.Column(db.String(255), nullable=False)
    is_active = db.Column(db.Boolean, nullable=False, default=True)
    is_deleted = db.Column(db.Boolean, nullable=False, default=False)

    productos = db.relationship('Producto', back_populates='categoria', lazy=True)

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'image': self.image,
            'description': self.description,
            'button_text': self.button_text,
            'url': self.url,
            'is_active': self.is_active,
            'is_deleted': self.is_deleted
        }