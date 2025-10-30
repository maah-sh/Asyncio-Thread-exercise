import asyncio
import aiofiles
from datetime import datetime

def get_output_line(input_line):
    input_line = input_line.rstrip()
    return input_line + ", " + str(len(input_line)) + "\n"

async def write_output_line(input_line, file):
    output_line = await asyncio.to_thread(get_output_line,input_line)
    await file.write(output_line)


async def main(input_path, output_path):
    async with aiofiles.open(input_path, mode='r') as input_file:
        async with aiofiles.open(output_path, mode='w') as output_file:
            input_lines = await input_file.readlines()
            await asyncio.gather(*(write_output_line(line, output_file) for line in input_lines))


if __name__ == '__main__':
    input_file_path = 'input_200k.txt'
    output_file_path = 'output.txt'

    start_time = datetime.now()

    asyncio.run(main(input_file_path, output_file_path))

    end_time = datetime.now()
    print('Run time: {}'.format(end_time - start_time))

