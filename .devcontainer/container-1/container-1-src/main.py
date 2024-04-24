from backend.backend import backend
from frontend.frontend import frontend
import asyncio


async def main():
  t1 = asyncio.create_task(backend())
  print("t1")
  t2 = asyncio.create_task(frontend())
  print("t2")
  await asyncio.gather(t1, t2)
  

if __name__ == "__main__":
  asyncio.run(main())