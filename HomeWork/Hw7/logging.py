def _log_(date, time, operation, input_data, result):
    with open('log.csv', 'a') as log_file:
        log_file.write(f'{date};{time};{input_data};{operation};{result}\n')
