import time
import asyncio

start = time.time()

async def fetch_file():
    print("starting to fetch file: ")
    await asyncio.sleep(1)
    print("fetching completed")

async def main():
    print("starting main")
    await asyncio.gather(  #executes all coroutines concurrently (no task defining)
    fetch_file(),
    fetch_file(),
    fetch_file()
    )
    print("main completed!")

asyncio.run(main())

end = time.time()
print("total time: ",end-start)