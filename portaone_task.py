""""

This is my task from Portaone

This code used for calculation:
    The maximum number in the file
    The minimum number in the file
    Median
    Arithmetic mean value
    The largest sequence of numbers (one after another) that increases (optional)
    The largest sequence of numbers (one by one) that decreases (optional)

REQUIREMENTS - install Python and Pandas Library
    
!!!By default file with data must be in the same folder as .py file!!!

!!! Data file must contained only one number per row and has no header. No data check!!!.

If your file have a different name please replace it in function call at the end(by default - 10m.txt )


"""


import pandas as pd
import time
import os

def data_read(file_name: str) -> pd.DataFrame:
    # Read data from file "name" in the same folder as .py script
    file_path : str = f'{os.path.join(os.path.dirname(__file__), file_name)}'
    data : pd.DataFrame = pd.read_csv(file_path, sep=" ", header=None)
    data.columns = ['Numbers']
    return data


def timer(func):
    # Measure execution time
    # Source https://stackoverflow.com/questions/77305875/python-get-the-total-execution-time-of-a-function
    def wrapper(*args, **kwargs):
        nonlocal total
        start = time.time()
        result = func(*args, **kwargs)
        duration = time.time() - start
        total += duration
        print(f"Execution time: {duration}   Total: {total}")
        return result

    total = 0
    return wrapper


@timer
def calculate_statistic_data(file_name: str = '10m.txt') -> None:
    # Read data from file
    data : pd.DataFrame = data_read(file_name)

    # Calulate first 4 values
    print(f' Max number: {data.max().to_string(index=False)}')   #  to_string(index=False) - to clean print, just value - no additional dataset information
    print(f'Min number: {data.min().to_string(index=False)}')
    print(f'Mediana: {data.median().to_string(index=False)}')
    print(f'Average: {data.mean().to_string(index=False)}')

    # Next function based on https://stackoverflow.com/questions/66955196/finding-longest-consecutive-increase-in-pandas

    # Add new columns that indicate umbers increasing
    data['is_increasing'] = data['Numbers'].diff().lt(0).cumsum()
    # Add new columns that indicate numbers decreasing
    data['is_decreasing'] = data['Numbers'].diff().gt(0).cumsum()
    # Creates an aggregate dataset with occurrence count values
    sizes_up = data.groupby('is_increasing')['Numbers'].transform('size')
    sizes_down = data.groupby('is_decreasing')['Numbers'].transform('size')
    # Filter and print dataset
    print(f'Max increasing sequence:\n{data["Numbers"][sizes_up == sizes_up.max()].to_string(index=False)}') 
    print(f'Max decreasing sequence:\n{data["Numbers"][sizes_down == sizes_down.max()].to_string(index=False)}')


if __name__ == "__main__":
    calculate_statistic_data('10m.txt')  #If your file have a different name please replace it in function call (by default - 10m.txt )
