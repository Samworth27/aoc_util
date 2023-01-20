import os
from collections.abc import Generator, Callable
import aocd

def fields(line:str, positions:list[int] = None, split_char:int=' ', field_func:Callable = lambda x: x) -> list:
    '''Splits a string into fields
    
    Parameters:
        line(str): The file line to be split into fields
        positions(list[int]): An array containing the indexes of positions to be returned
            If left empty will return all positions
        split_char(str) : The character to separate fields
        field_func(function): A function applied to every field
    '''
    return [field_func(field) for position, field in enumerate(line.split(split_char)) if positions is None or position in positions]

def parse_input(source:tuple[int,int]|str, parse_func:Callable = lambda x: x):
    '''Processes input data using a supplied function
    
    Parameters:
        source (tuple(day:int,year:int): Fetches data from the AoC website for that day and year
        or
        source (str): Fetches data from a test case stored in './test_cases'
        parse_func (function): A function to be applied to every row of the file
    '''
    return [parse_func(row) for row in get_data(source)]

def get_data(source:tuple[int,int]|str):
    '''Fetches data from either the real input from the AoC website or local test cases 
    
    Parameters:
        source (tuple(day:int,year:int): Fetches data from the AoC website for that day and year
        or
        source (str): Fetches data from a test case stored in './test_cases'
    '''
    match source:
        case tuple(source):
            if len(source) != 2:
                raise SyntaxError(f"Length of source should be 2. Was {len(source)}")
            for var in source:
                if type(var) != int:
                    raise ValueError(f"Expected type(int) but got type({type(var).__name__})")
            data = aocd.get_data(day=source[0],year=source[1]).split('\n')
        
        case str(source):
            data = list(read_file(source))
            
        case _:
            raise TypeError("Valid input not given")
            
    return data

def read_file(test_case='example') -> Generator[str]:
    '''Reads files located at "./test_cases"
    
    Parameters:
        test_case (str): The name of the test case file
    '''
    path = f'{os.getcwd()}/test_cases/{test_case}.txt'
    with open(path) as file:
        for line in file:
            yield line.strip('\n')