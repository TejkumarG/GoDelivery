from enum import Enum

from pydantic import BaseModel, UUID4, constr
from typing import Optional


class ShipperBase(BaseModel):
    name: str
    address: Optional[str]
    contact_information: str = ''


class ShipperCreate(ShipperBase):
    pass


class Shipper(ShipperBase):
    id: int

    class Config:
        from_attributes = True


class StatusEnum(str, Enum):
    Shipped = "Shipped"
    InTransit = "In Transit"
    Delivered = "Delivered"
    Cancelled = "Cancelled"


class PackageBase(BaseModel):
    tracking_number: str
    status: str = StatusEnum.Shipped
    delivery_address: Optional[str]
    weight: float
    shipper_id: Optional[int]


class PackageCreate(PackageBase):
    pass


class Package(PackageBase):
    id: int
    shipper: Shipper

    class Config:
        from_attributes = True
