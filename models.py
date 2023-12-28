import uuid

from sqlalchemy import (
    String,
    Enum, DECIMAL, Integer, Column, ForeignKey, UUID
)
from sqlalchemy.orm import relationship

from database import Base


class Shipper(Base):
    __tablename__ = "shippers"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, unique=True, index=True)
    address = Column(String)
    contact_information = Column(String, default='')

    packages = relationship("Package", back_populates="shipper")


class Package(Base):
    __tablename__ = "packages"

    id = Column(Integer, primary_key=True, autoincrement=True)
    tracking_number = Column(String(100), unique=True)
    status = Column(Enum('Shipped', 'In Transit', 'Delivered', 'Cancelled'), default='Shipped')
    delivery_address = Column(String(255))
    weight = Column(DECIMAL(10, 2))

    shipper_id = Column(Integer, ForeignKey('shippers.id'), nullable=True)
    shipper = relationship("Shipper", back_populates='packages')
