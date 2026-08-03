from typing import Any
from enum import Enum
from schemas import Shipment
from fastapi import FastAPI, HTTPException, status
from scalar_fastapi import get_scalar_api_reference



app = FastAPI()
    
### Shipments datastore as dict
shipments = {
    12701: {"weight": 0.6, "content": "rubber ducks", "status": "placed", "destination": "New York"},
    12702: {"weight": 2.3, "content": "magic wands", "status": "shipped", "destination": "Los Angeles"},
    12703: {"weight": 1.1, "content": "unicorn horns", "status": "delivered", "destination": "Chicago"},
    12704: {"weight": 3.5, "content": "dragon eggs", "status": "in transit", "destination": "Miami"},
    12705: {"weight": 0.9, "content": "wizard hats", "status": "returned", "destination": "Seattle"},
}


### Read a shipment by id
@app.get("/shipment")
def get_shipment(id: int) -> dict[str, Any]:
    # Check for shipment with given id
    if id not in shipments:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Given id doesn't exist!",
        )

    return shipments[id]


### Create a new shipment with content and weight
@app.post("/shipment")
def submit_shipment(shipment: Shipment) -> dict[str, int]:
    
    # Create and assign shipment a new id
    new_id = max(shipments.keys()) + 1
    # Add to shipments dict
    shipments[new_id] = {
        "content": shipment.content,
        "weight": shipment.weight,
        "destination": shipment.destination,
        "status": "placed",
    }
    # Return id for later use
    return {"id": new_id}

class ShipmentStatus(str, Enum):
    placed = "placed"
    in_transit = "in transit"
    shipped = "shipped"
    out_for_delivery = "out for delivery"
    delivered = "delivered"
    returned = "returned"

### Update fields of a shipment
@app.patch("/shipment")
def update_shipment(id: int, body: dict[str, ShipmentStatus]) -> dict[str, Any]:
    # Update data with given fields
    shipments[id].update(body)
    return shipments[id]


### Delete a shipment by id
@app.delete("/shipment")
def delete_shipment(id: int) -> dict[str, str]:
    # Remove from datastore
    shipments.pop(id)

    return {"detail": f"Shipment with id #{id} is deleted!"}


### Scalar API Documentation
@app.get("/scalar", include_in_schema=False)
def get_scalar_docs():
    return get_scalar_api_reference(
        openapi_url=app.openapi_url,
        title="Scalar API",
    )
