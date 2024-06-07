from utils.db import db
from uuid import uuid4

def generate_uuid():
    return str(uuid4())


class Product(db.Model):
    __tablename__ = "products"

    id = db.Column(
        db.String(255),
        nullable=False,
        unique=True,
        default=generate_uuid,
        primary_key=True,
    )
    name = db.Column(db.String(100), unique=True, nullable=False)
    description = db.Column(db.String(200), nullable=False)
    created_at = db.Column(
        db.DateTime(timezone=True), default=db.func.current_timestamp(), nullable=False
    )
    updated_at = db.Column(
        db.DateTime(timezone=True),
        default=db.func.current_timestamp(),
        onupdate=db.func.current_timestamp(),
        nullable=False,
    )

    def __init__(self, name, description):
        self.name = name
        self.description = description
