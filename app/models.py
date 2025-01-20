from .db_connection import Base
from sqlalchemy import Column, Integer, String, Boolean, CheckConstraint, UniqueConstraint, text, DateTime, ForeignKey, Enum, Text
from sqlalchemy.dialects.postgresql import UUID
import sqlalchemy



class Category(Base):
    __tablename__ = "category"

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(100), nullable=False)
    slug = Column(String(120), nullable=False)
    is_active = Column(Boolean, nullable=False, default=False, server_default="False")
    level = Column(Integer, nullable=False, default="100", server_default="100")
    parent_id = Column(Integer, ForeignKey("category.id"), nullable=True)


    __table_args__ = (
        CheckConstraint("LENGTH(name) > 0", name="category_name_length_check"),   
        CheckConstraint("LENGTH(slug) > 0", name="category_slug_length_check"),   
        UniqueConstraint("name", "level", name="uq_category_name_level"),
        UniqueConstraint("slug", name="uq_category_slug"), 
    )

class Product(Base):
    __tablename__ = "product"

    id = Column(Integer, primary_key=True, nullable=False)
    pid = Column(UUID(as_uuid=True), unique=True, nullable=False, server_default=text("uuid_generate_v4()"))
    name = Column(String(200), nullable=False)
    slug = Column(String(220), nullable=False)
    description = Column(Text, nullable=True)
    is_digital = Column(Boolean, nullable=False)
    created_at = Column(DateTime, server_default=text("CURRENT_TIMESTAMP") ,nullable=False)
    updated_at = Column(DateTime, server_default=text("CURRENT_TIMESTAMP"), onupdate=sqlalchemy.func.now(), nullable=False)
    is_active = Column(Boolean, nullable=False, default=False, server_default="False")
    stock_status = Column(Enum("oos","is", "obo", name= "status_enum"), server_default="oos", nullable=False)
    category_id = Column(Integer, ForeignKey("category.id"), nullable=False)

    __table_args__ = (
        CheckConstraint("LENGTH(name) > 0", name="product_name_length_check"),   
        CheckConstraint("LENGTH(slug) > 0", name="product_slug_length_check"),   
        UniqueConstraint("name", name="uq_product_name"),
        UniqueConstraint("slug", name="uq_product_slug"), 
    )



    