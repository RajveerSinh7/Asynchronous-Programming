import time
import asyncio

start = time.time()

async def get_movie_tickets():
    await asyncio.sleep(3)
    print("got the movie tickets")

async def use_instagram():
    await asyncio.sleep(1)
    print("opened instagram")

async def main():
    task1 = asyncio.create_task(get_movie_tickets())
    task2 = asyncio.create_task(use_instagram())
    await task1
    await task2

asyncio.run(main())

end = time.time()
print('time of execution: ', (end-start))