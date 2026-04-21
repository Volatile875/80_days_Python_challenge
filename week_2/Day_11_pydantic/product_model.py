from pydantic import BaseModel
# from fastapi import FastAPI

# app = FastAPI()
class Product(BaseModel):
    id: int
    name: str
    price: float
    in_stock: bool = True


product_one = Product(id=1, name="Laptop", price=999, in_stock=True)

product_two = Product(id=2, name="Mouse", price=24)

product_three = Product (name="keyword")