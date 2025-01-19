from .db_connection import Base
from sqlalchemy import Column, Integer, String, Boolean, CheckConstraint, UniqueConstraint
from sqlalchemy.dialects.postgresql import UUID


class Category(Base):
    __tablename__ = "category"

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(100), nullable=False)
    slug = Column(String(120), nullable=False)
    is_active = Column(Boolean, nullable=False, default=False, server_default="False")
    level = Column(Integer, nullable=False, default="100", server_default="100")
    parent_id = Column(Integer, nullable=True)


    __table_args__ = (
        CheckConstraint("LENGTH(name) > 0", name="category_name_length_check"),   
        CheckConstraint("LENGTH(slug) > 0", name="category_slug_length_check"),   
        UniqueConstraint("name", "level", name="uq_category_name_level"),
        UniqueConstraint("slug", name="uq_category_slug"), 
    )

class Product(Base):
    __tablename__ = "product"

    id = Column(Integer, primary_key=True, nullable=False)
    pid = Column(UUID, nullable=False)
    name = Column(String(200), nullable=False)
    slug = Column(String(220), nullable=False)
    description = Column(String)
    is_digital = Column(Boolean, nullable=False)
    created_at = Column()
    updated_at = Column()
    is_active = Column(Boolean, nullable=False)
    stock_status = Column(String)
    category_id = Column()



    