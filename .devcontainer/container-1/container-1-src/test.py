import asyncio

async def main():
  t1 = asyncio.create_task(frontend())
  t2 = asyncio.create_task(backend())
  await asyncio.gather(t1, t2)
  
async def frontend():
  while True:
    print("frontend")
    await asyncio.sleep(10)
    
async def backend():
  while True:
    print("backend")
    asyncio.sleep(10)
    
asyncio.run(main())