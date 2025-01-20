import asyncio as aio


async def main():
    future = aio.Future()
    aio.create_task(
        coro(future)
    )  # Creating a task that will set the result of 'future'
    await future  # This will "block" until 'future' gets a result or exception
    coro_result = future.result()  # Retrieves the result of 'future' once it's set
    print(coro_result)
