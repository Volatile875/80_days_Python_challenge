from pydantic import Field,BaseModel, computed_field
from fastapi import FastAPI


app=FastAPI()


class Booking(BaseModel):
    user_id: int
    room_id: int 
    nights: int = Field(..., ge=1)
    rate_per_night: int

    @computed_field
    @property
    def total_amount(self) -> float:
        return self.nights * self.rate_per_night

booking = Booking(
    user_id=123,
    room_id=456,
    nights=3,
    rate_per_night=100.00,

)

print(booking.total_amount)
print(booking.model_dump())