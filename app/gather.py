import asyncio
import time


async def task1():
    print("Task1 Start")
    await asyncio.sleep(2)
    print("Task1 Done")


async def task2():
    print("Task2 Start")
    await asyncio.sleep(4)
    print("Task2 Done")


async def main():
    await asyncio.gather(task1(), task2())


asyncio.run(main())