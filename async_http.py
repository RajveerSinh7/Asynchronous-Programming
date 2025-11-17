import aiohttp
import asyncio
import time
import requests

start_time = time.time() 
async def main():
    async with aiohttp.ClientSession() as session: #create session
        for i in range(1,151):
            url = 'https://pokeapi.co/api/v2/pokemon/' + str(i)
            async with session.get(url) as resp: #sending req
                pokemon = await resp.json() #continue running and not wait 
                print(pokemon['name']) 


asyncio.run(main())
end_time = time.time()

print("execution = ",end_time-start_time)
#execution =  3.2184979915618896