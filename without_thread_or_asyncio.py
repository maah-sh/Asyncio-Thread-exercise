from datetime import datetime


if __name__ == '__main__':
    input_file_path = 'input.txt'
    output_file_path = 'output.txt'

    start_time = datetime.now()

    open(output_file_path, 'w').close()
    with open(input_file_path) as file:
        for line in file:
            input_line = line.rstrip()

            with open(output_file_path, 'a') as output_file:
                new_line = input_line + ", " + str(len(input_line)) + "\n"
                output_file.write(new_line)

    end_time = datetime.now()
    print('Run time: {}'.format(end_time - start_time))