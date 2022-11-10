
from time import strftime

def _log_(operation, number_1, number_2, result):
    with open('log.csv', 'a') as log_file:
        log_file.write(f'{strftime("%x")};{strftime("%X")};{number_1};{operation};{number_2};{result}\n')