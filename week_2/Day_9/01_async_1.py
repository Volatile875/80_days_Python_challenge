import asyncio
import time
from aioconsole import aprint

async def brew_chai():
    await print("Brewing_chai...")
    await asyncio.sleep(2)
    await print("Chai is ready1!")

asyncio.run(brew_chai())


    



# import asyncio

# async def brew_chai():
#     print("Brewing_chai...")
#     await asyncio.sleep(2)
#     print("Chai is ready1!")

# asyncio.run(brew_chai()