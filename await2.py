import asyncio

async def bake_cake():
    print("baking cake")
    await asyncio.sleep(2)
    print("cake ready")

async def make_juice():
    print("making juice")
    await asyncio.sleep(1)
    print("juice ready")

async def main():
    task1 = asyncio.create_task(bake_cake())
    task2 = asyncio.create_task(make_juice())
    await task1
    await task2
asyncio.run(main())
