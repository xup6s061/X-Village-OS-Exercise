import threading
import numpy as np
import time
import random

a=1000

matA = np.random.randint(10, size = (a, a))
matB = np.random.randint(10, size = (a, a))
result = np.zeros((matA.shape[0], matB.shape[1]))
start_time_numpy = time.time()
result_co = np.matmul(matA, matB)
end_time_numpy = time.time()

def thread_func(i ,num1, num2, thread_num): 
    for j in range(i*(int(a/thread_num)) ,i*(int(a/thread_num))+(int(a/thread_num))):
        result[j] = np.matmul(matA[j], matB)

def main():
    # How many thread you want to use
    thread_num = 10
    processes = thread_num
    threads = []
    start_time = time.time()

    jobs = []
    # Assign job to threads

    for i in range(0 ,thread_num):
        # Pass argument to function with tuple
        thread = threading.Thread(target = thread_func, args = (i ,matA[i], matB, thread_num))
        threads.append(thread)

    # run all threads
    for thread in threads:
        thread.start()

    # Wait for threads finish
    for thread in threads:
        thread.join()
    # print(result)
    # print(result_co)
    end_time = time.time()
    print('Is answer right:', result == result_co)
    print('Time elapsed:\t', end_time - start_time)
    print('Numpy time elapsed:\t', end_time_numpy - start_time_numpy)

if __name__ == "__main__":
    main()

# print('Numpy time elapsed:\t', end_time_numpy - start_time_numpy)

