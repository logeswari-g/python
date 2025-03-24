import asyncio
import gc

async def heavy_task():
    large_object = [0] * 10**6  # Allocate a large object
    await asyncio.sleep(1)  # Simulate I/O operation
    print("Task completed")
    del large_object  # Manually free memory
    gc.collect()  # Trigger garbage collection

async def main():
    tasks = [asyncio.create_task(heavy_task()) for _ in range(5)]
    await asyncio.gather(*tasks)

asyncio.run(main())
