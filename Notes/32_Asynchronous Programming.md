### What is Asynchronous Programming?

Asynchronous programming lets your program **continue doing other things while waiting** — especially useful when dealing with slow tasks like API calls, file access, or database queries.

### Key Concepts

| Term        | Description |
|-------------|-------------|
| `async def` | Defines an asynchronous function |
| `await`     | Tells Python to pause here and wait for something (non-blocking) |
| Event loop  | The engine that runs and manages async tasks |
| `asyncio`   | Built-in module for writing async code |

### When to Use Async

- Making **multiple API calls**
- Reading or writing to files
- Downloading or uploading files
- Working with **many users** or clients at once

### Example: Simulated API Calls

```python
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
```

---
