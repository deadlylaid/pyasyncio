import asyncio
import aiofiles


async def read_file(file_path):
    async with aiofiles.open(file_path, mode='r') as _file:
        content = await _file.read()
    return content


async def main():
    file_path = ['file1.txt', 'file2.txt', 'file3.txt']
    read_tasks = [read_file(_file) for _file in file_path]

    # 이 코드를 통해서 file1.txt, file2.txt, file3.txt 파일 내용을 비동기로 읽어온다
    contents = await asyncio.gather(*read_tasks)
    for content in contents:
        print(content)


asyncio.run(main())