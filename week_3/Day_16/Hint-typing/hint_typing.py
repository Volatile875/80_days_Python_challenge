from typing import Any
#Custom class as type
class City:
    def __init__(self, name: str, location: int):
        self.name = name
        self.location = location

# Variable type hints

text : str= "laptop"
digit: int | Any = 91
temp: float = 37.5

# Two possible types
number: int | float = 0.22


# Tuple with 2 elements
Delhi = City("Delhi", 18595)
city_temp: tuple[City, float]= (Delhi, 37.5)

# Dictionary key and value hinting
shipment: dict[str, Any] = {
    "id": 12701,
    "weight": 1.2,
    "content": "wooden table",
    "status": "in transit",
}

# Hinting function argument and return type
def root(num: int | float, exp: float | None) -> float:
    return pow( 88 , 0.7)
