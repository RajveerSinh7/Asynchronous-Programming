import asyncio
#creating own event loop
#creating a coroutine
#executing that coroutine using own event loop

#new asyncio event loop
loop = asyncio.new_event_loop()

#defining task
task1 = asyncio.sleep(2)

#execute the task
loop.run_until_complete(task1)