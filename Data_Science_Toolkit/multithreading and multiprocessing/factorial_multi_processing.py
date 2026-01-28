'''
Real-World Example: Multiprocessing for CPU-bound Tasks
Scenario: Factorial Calculation
Factorial calculations, especially for large numbers, 
involve significant computational work. Multiprocessing 
can be used to distribute the workload across multiple 
CPU cores, improving performance.

'''
import multiprocessing
import math
import sys
import time

# digits for integer conversion
sys.set_int_max_str_digits(1000000)

# function to compute factorial

def compute_factorials(number):
    print(f"Computing factorial for: {number}")
    result = math.factorial(number)
    print(f"Factorial of {number} is {result}")
    return result

if __name__ == '__main__':
    numbers = [10000, 20000, 30000, 40000]

    start_time = time.time()

    #  create a pool of worker processes
    with multiprocessing.Pool() as pool:
        results = pool.map(compute_factorials, numbers)

    
    end_time = time.time()
    print(f"Results: {results}")
    print(f"Time taken : {end_time - start_time} seconds")