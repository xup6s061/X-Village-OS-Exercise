import numpy as np
import time
import multiprocessing
import random

a=1000

def process_func(i ,num1, num2, thread_num, result_queue):
    for j in range(i*(int(a/thread_num)) ,i*(int(a/thread_num))+(int(a/thread_num))):
        result_queue.put((j, np.matmul(num1[j], num2)))

def main():
    # How many thread you want to use
    #=========================================normal setting==========================================

    matA = np.random.randint(10, size = (a, a))
    matB = np.random.randint(10, size = (a, a))
    result = np.zeros((matA.shape[0], matB.shape[1]))
    start_time_numpy = time.time()
    result_co = np.matmul(matA, matB)
    end_time_numpy = time.time()
    #=========================================process setting==========================================
    result_process = []
    result_process_final = []
    processes = 10
    result_queue = multiprocessing.Manager().Queue()
    jobs = []
    # Assign job to threads
    #=========================================strat process==========================================
    start_time_process = time.time()
    for i in range(0 ,processes):
        process = multiprocessing.Process(target = process_func, args = (i ,matA, matB, processes, result_queue))
        jobs.append(process)

    for process in jobs:
        process.start()

    for process in jobs:
        process.join()

    while not result_queue.empty():
        result_process.append(result_queue.get())
    for k in range(0, len(result_process)):
        result_process_final.append(sorted(result_process)[k][1])
    print('Is answer right:', result_process_final == result_co)
    # print(sorted(result_process))
    # print(result_co)
    end_time_process = time.time()
    print('Process time elapsed:\t', end_time_process - start_time_process)
    print('Numpy time elapsed:\t', end_time_numpy - start_time_numpy)
if __name__ == "__main__":
    main()



