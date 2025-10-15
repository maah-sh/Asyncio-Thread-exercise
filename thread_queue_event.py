from datetime import datetime
import queue
import threading
from concurrent.futures import ThreadPoolExecutor


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


if __name__ == '__main__':
    input_file_path = 'input.txt'
    output_file_path = 'output.txt'

    start_time = datetime.now()

    queue_object = queue.Queue()
    event = threading.Event()
    with ThreadPoolExecutor(max_workers=2) as executor:
        executor.submit(read_input_file, input_file_path, queue_object, event)
        executor.submit(write_output_file, output_file_path, queue_object, event)

    end_time = datetime.now()
    print('Run time: {}'.format(end_time - start_time))