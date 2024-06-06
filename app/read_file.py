import asyncio
import aiofiles


async def read_file():
    async with aiofiles.open("example.txt", mode="r") as _file:
        content = await _file.read()
    return content


async def main():
    content = await read_file()
    print(content)


asyncio.run(main())
