from datetime import datetime
from concurrent.futures import ThreadPoolExecutor
from itertools import repeat


def write_output_line(input_line, file):
    input_line = input_line.rstrip()
    output_line = input_line + ", " + str(len(input_line)) + "\n"
    file.write(output_line)


if __name__ == '__main__':
    input_file_path = 'input.txt'
    output_file_path = 'output.txt'

    start_time = datetime.now()

    with open(input_file_path) as input_file:
        with open(output_file_path, 'w') as output_file:
            with ThreadPoolExecutor(max_workers=5) as executor:
                executor.map(write_output_line, input_file, repeat(output_file))

    end_time = datetime.now()
    print('Run time: {}'.format(end_time - start_time))