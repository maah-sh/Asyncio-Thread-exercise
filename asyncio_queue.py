import asyncio
import aiofiles
from datetime import datetime

async def read_input_file(input_file, queue):
    async with aiofiles.open(input_file, mode='r') as file:
        async for line in file:
            await queue.put(line.rstrip())



async def write_output_file(output_file, queue, read_task):
    open(output_file, 'w').close()
    while not read_task.done() or not queue.empty():
        async with aiofiles.open(output_file, mode='a') as file:
            input_line = await queue.get()
            new_line = input_line + ", " + str(len(input_line)) + "\n"
            await file.write(new_line)
            queue.task_done()

async def main(input_file, output_file):
    asyncio_queue = asyncio.Queue()
    read_task = asyncio.create_task(read_input_file(input_file, asyncio_queue))
    write_task = asyncio.create_task(write_output_file(output_file, asyncio_queue, read_task))
    await asyncio.gather(read_task, write_task)
    await asyncio_queue.join()



if __name__ == '__main__':
    input_file_path = 'input.txt'
    output_file_path = 'output.txt'

    start_time = datetime.now()

    asyncio.run(main(input_file_path, output_file_path))

    end_time = datetime.now()
    print('Run time: {}'.format(end_time - start_time))

