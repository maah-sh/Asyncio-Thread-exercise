import asyncio
import aiofiles
import threading
from datetime import datetime

async def read_input_file(input_file):
    async with aiofiles.open(input_file, mode='r') as file:
        async for line in file:
            yield line.rstrip()


async def write_output_file(input_file, output_file):
    async with aiofiles.open(output_file, mode='w') as file:
        async for input_line in read_input_file(input_file):
            new_line = input_line + ", " + str(len(input_line)) + "\n"
            await file.write(new_line)



if __name__ == '__main__':
    input_file_path = 'input.txt'
    output_file_path = 'output.txt'

    start_time = datetime.now()

    asyncio.run(write_output_file(input_file_path, output_file_path))

    end_time = datetime.now()
    print('Run time: {}'.format(end_time - start_time))

