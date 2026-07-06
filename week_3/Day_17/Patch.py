from typing import Any

from fastapi import FastAPI, status, HTTPException, Query, Path
from scalar_fastapi import get_scalar_api_reference


app = FastAPI()

shipments = {
    12701: {
        "weight": .6,
        "content": "glassware",
        "status": "placed"
    },
    12702: {
        "weight": 2.3,
        "content": "books",
        "status": "shipped"
    },
    12703: {
        "weight": 1.1,
        "content": "electronics",
        "status": "delivered"
    },
    12704: {
        "weight": 3.5,
        "content": "furniture",
        "status": "in transit"
    },
    12705: {
        "weight": .9,
        "content": "clothing",
        "status": "returned"
    },
    12706: {
        "weight": 4.0,
        "content": "appliances",
        "status": "processing"
    },
    12707: {
        "weight": 1.8,
        "content": "toys",
        "status": "placed"
    },
}






@app.get("/shipment")
def get_shipment(id: int) -> dict[str, Any]:

    if id not in shipments:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Given id does not exist in shipments"

        )
       

    return shipments[id]



@app.post("/shipment")
def submit_shipment(data: dict[str, Any]) -> dict[str, Any]:
    content = data["content"]
    weight = data["weight"]

    if weight > 25:
        raise HTTPException(
            status_code=status.HTTP_406_NOT_ACCEPTABLE,
            detail="Weight cannot exceed 25"
        )

    new_id = max(shipments.keys()) + 1

    shipments[new_id] = {
        "content": content,
        "weight": weight,
        "status": "placed"
    }

    return {"id": new_id, **shipments[new_id]}


@app.get("/shipments/{field}/{id}")
def get_shipment_field(field: str, id: int) -> dict[str, Any]: 
    return {
        field : shipments[id][field]
    }

@app.put("/shipment")
def shipment_update(id: int, content: str, weight: float, status: str) -> dict[str,Any]:
    shipments[id]={
        "content": content,
        "weight": weight,
        "status": "placed",  
        }
    return shipments[id]


@app.patch("/shipment")
def patch_shipment(
    id: int,
    content: str | None = None,
    weight: float | None = None,
    shipment_status: str | None = None
):

    shipment = shipments.get(id)
    if not shipment:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Given id does not exist in shipments"
        )

    if content is not None:
        shipment["content"] = content
    if weight is not None:
        shipment["weight"] = weight
    if shipment_status is not None:
        shipment["status"] = shipment_status

    shipments[id]= shipment
    return shipments




# Scalar API Documentation
@app.get("/scalar", include_in_schema=False)
def get_scalar_docs():
    return get_scalar_api_reference(
        openapi_url=app.openapi_url,
        title="Scalar API",
    )