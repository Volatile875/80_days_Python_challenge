from typing import Any
from .schemas import ShipmentUpdate, ShipmentCreate, ShipmentStatus
from fastapi import FastAPI, HTTPException, status
from .database import Database

app = FastAPI()

db = Database()
    
### Shipments datastore as dict
shipments = {
    12701: {"weight": 0.6, "content": "rubber ducks", "status": "placed", "destination": "New York"},
    12702: {"weight": 2.3, "content": "magic wands", "status": "shipped", "destination": "Los Angeles"},
    12703: {"weight": 1.1, "content": "unicorn horns", "status": "delivered", "destination": "Chicago"},
    12704: {"weight": 3.5, "content": "dragon eggs", "status": "in transit", "destination": "Miami"},
    12705: {"weight": 0.9, "content": "wizard hats", "status": "returned", "destination": "Seattle"},
}


### Read a shipment by id
@app.get("/shipment", response_model= ShipmentStatus)
def get_shipment(id:int):
    # Check for shipment with given id
    shipment = db.get(id)

    if shipment is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Given id doesn't exist!",
        )

    return shipment


### Create a new shipment with content and weight
@app.post("/shipment", response_model = None)

def submit_shipment(shipment: ShipmentCreate) -> dict[str, int]:
    # Create and assign shipment a new id
    new_id = db.create(shipment)
    # Return id for later use
    return {"id": new_id}


### Update fields of a shipment
@app.patch("/shipment", response_model = ShipmentStatus)
def update_shipment(self, id: int, shipment: ShipmentUpdate):
    # Update data with given fields
    shipment = db.update(id, shipment)
    return shipment


### Delete a shipment by id
@app.delete("/shipment")
def delete_shipment(id: int) -> dict[str, str]:
    # Remove from datastore
    shipments.pop(id)

    return {"detail": f"Shipment with id #{id} is deleted!"}


### Scalar API Documentation
@app.get("/scalar", include_in_schema=False)
def get_scalar_docs():
    return app.openapi()
