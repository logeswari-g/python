import asyncio

async def fetch_data(site):
    print(f"Fetching from {site}...")
    await asyncio.sleep(2)
    print(f"Done fetching from {site}")

async def main():
    await asyncio.gather(
        fetch_data("Site A"),
        fetch_data("Site B"),
        fetch_data("Site C"),
    )

asyncio.run(main())
