from typing import Optional
from enum import Enum
from pydantic import BaseModel, Field


class ShipmentStatus(str, Enum):
    placed = "placed"
    in_transit = "in transit"
    shipped = "shipped"
    out_for_delivery = "out for delivery"
    delivered = "delivered"
    returned = "returned"


class Shipment(BaseModel):
    content: str
    weight: float = Field(lt=25)
    destination: str


class ShipmentCreate(Shipment):
    status: ShipmentStatus = ShipmentStatus.placed


class ShipmentUpdate(BaseModel):
    content: Optional[str] = None
    weight: Optional[float] = Field(default=None, lt=25)
    destination: Optional[str] = None
    status: Optional[ShipmentStatus] = None

