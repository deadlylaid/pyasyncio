import asyncio
import aiofiles


async def write_file(file_path, content):
    async with aiofiles.open(file_path, mode="w") as _file:
        await _file.write(content)


async def main(file_path, content):
    await write_file(file_path, content)


asyncio.run(main('file.txt', 'Hello, World!'))
