import asyncio
from aioconsole import aprint # Using the async print library you imported

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("hi this is pratik!")
    
    async def mohit(self):
        await asyncio.sleep(20) # Shortened for testing
        # Use aprint here since you imported it
        await aprint(f"Welcome {self.name}")

# 1. Create the object first
ob1 = Person("sid", 29)

# 2. Run the specific method of that object
asyncio.run(ob1.mohit())
