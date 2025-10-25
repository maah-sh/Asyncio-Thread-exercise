import asyncio
import queue
import threading
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime

def read_input_file(input_file, queue_obj, reading_end_event):
    with open(input_file) as file:
        for line in file:
            queue_obj.put(line.rstrip())

    reading_end_event.set()

def write_output_file(output_file, queue_obj, reading_end_event):
    open(output_file, 'w').close()
    while not reading_end_event.is_set() or not queue_obj.empty():
        with open(output_file, 'a') as file:
            input_line = queue_obj.get()
            output_line = input_line + ", " + str(len(input_line)) + "\n"
            file.write(output_line)

async def main(input_file, output_file):
    loop = asyncio.get_running_loop()
    queue_obj = queue.Queue()
    event = threading.Event()

    with ThreadPoolExecutor(max_workers=2) as pool:
        read_task = loop.run_in_executor(pool, read_input_file, input_file, queue_obj, event)
        write_task =  loop.run_in_executor(pool, write_output_file, output_file, queue_obj, event)

    await asyncio.gather(read_task, write_task)


if __name__ == '__main__':
    input_file_path = 'input.txt'
    output_file_path = 'output.txt'

    start_time = datetime.now()

    asyncio.run(main(input_file_path, output_file_path))

    end_time = datetime.now()
    print('Run time: {}'.format(end_time - start_time))