from datetime import datetime
from concurrent.futures import ThreadPoolExecutor
from itertools import repeat
from time import sleep


def get_input_lines(line):
    return line.rstrip()

def get_output_line(input_line):
    input_line = input_line.rstrip()
    output_line = input_line + ", " + str(len(input_line)) + "\n"
    return output_line


if __name__ == '__main__':
    input_file_path = 'input_200k.txt'
    output_file_path = 'output.txt'

    start_time = datetime.now()

    with open(input_file_path) as input_file:
        with ThreadPoolExecutor(max_workers=5) as executor:
            input_lines = list(executor.map(get_input_lines, input_file))

    with open(output_file_path, 'w') as output_file:
        with ThreadPoolExecutor(max_workers=5) as executor:
            output_lines = list(executor.map(get_output_line, input_lines))
            output_file.writelines(output_lines)

    end_time = datetime.now()
    print('Run time: {}'.format(end_time - start_time))