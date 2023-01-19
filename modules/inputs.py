import os
from collections.abc import Generator

def fields(line:str, positions:list[int] = None, split_char=' ', field_func = lambda x: x) -> list:
    return [field_func(field) for position, field in enumerate(line.split(split_char)) if positions is None or position in positions]

def parse_input(example=False, test_case='example', function = lambda x: x):
    '''Reads and processes input files located in './test_cases'
    
    Parameters:
        example (bool): Use an example test case. If false 'input.txt' will be opened
        test_case (str): The name of the test case file
        function (function): A function to be applied to every row of the file
    '''
    return [function(row) for row in read_file(example, test_case)]


def read_file(example=False, test_case='example') -> Generator[str]:
    '''Reads files located at "./test_cases"
    
    Parameters:
        example (bool): Use an example test case. If false 'input.txt' will be opened
        test_case (str): The name of the test case file
    '''
    path = f'{os.getcwd()}/test_cases/tc_{test_case}.txt' if example else f"{os.getcwd()}/test_cases/input.txt"
    with open(path) as file:
        for line in file:
            yield line.strip('\n')
