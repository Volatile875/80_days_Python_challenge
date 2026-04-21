import asyncio
import time

async def brew(name):
    print(f"Brewing {name} coffee...")
    #await asyncio.sleep(3)
    time.sleep(3)
    print(f" {name} is ready...")

async def main():
    await asyncio.gather(
        brew("Masala coffee"),
        brew("black coffee"),
        brew("green coffee"),

    )

asyncio.run(main())
