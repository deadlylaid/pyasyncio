import asyncio
import time


async def task1():
    print("10초 뒤 출발!")
    await asyncio.sleep(10)
    print("10초 됬다!")


async def task2():
    print("1초 뒤 출발!")
    time.sleep(1)
    print("1초 됬다!")


async def main():
    await asyncio.gather(task1(), task2())


asyncio.run(main())
