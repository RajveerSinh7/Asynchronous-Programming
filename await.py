import asyncio

async def bake_cake():
    print("Baking cake...")
    await asyncio.sleep(2)
    print("Cake ready!")

async def chop_veggies():
    print("Chopping veggies...")
    await asyncio.sleep(1)
    print("Veggies ready!")

async def main():
    # Start both tasks concurrently
    task1 = asyncio.create_task(bake_cake())
    task2 = asyncio.create_task(chop_veggies())

    # Wait for both to finish
    await task1
    await task2

asyncio.run(main())