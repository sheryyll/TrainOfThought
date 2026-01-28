# processes that run in parallel
# used during: CPU bound tasks, Parallel execution

import multiprocessing
import time

def square_numbers():
    for i in range(5):
        time.sleep(1)
        print(f"Square : {i*i}")


def cube_numbers():
    for i in range(5):
        time.sleep(1.5)
        print(f"Cube : {i*i*i}")


if __name__ == "__main__":

    # create 2 processes
    p1 = multiprocessing.Process(target=square_numbers)
    p2 = multiprocessing.Process(target=cube_numbers)

    t = time.time()
    #  start the processes
    p1.start()
    p2.start()

    #  wait for the process to complete
    p1.join()
    p2.join()

    finished_time = time.time() - t
    print(f"Finished in: {finished_time} seconds")


