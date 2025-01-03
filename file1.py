import time
import multiprocessing
import threading

# Function to perform dummy processing
def do_something(size, out_list):
    # Dummy processing for demonstration
    for i in range(size):
        out_list.append(i * i)

if __name__ == "__main__":  # Correcting special variable check
    size = 100000  # Fixed size assignment
    procs = 10
    jobs = []

    # Multiprocessing
    start_time = time.time()
    manager = multiprocessing.Manager()  # Manager to create a shared list
    out_list = manager.list()  # Shared list across processes

    for i in range(procs):
        process = multiprocessing.Process(target=do_something, args=(size, out_list))
        jobs.append(process)

    for j in jobs:
        j.start()

    for j in jobs:
        j.join()

    print("List processing complete (Multiprocessing).")
    end_time = time.time()
    print(f"Multiprocessing time: {end_time - start_time} seconds")

    # Reset jobs list for threading
    jobs = []
    out_list = []  # Local list for threads, threads share memory space by default
    threads = 10
    start_time = time.time()

    for k in range(threads):
        thread = threading.Thread(target=do_something, args=(size, out_list))
        jobs.append(thread)

    for l in jobs:
        l.start()

    for l in jobs:
        l.join()

    print("List processing complete (Multithreading).")
    end_time = time.time()
    print(f"Multithreading time: {end_time - start_time} seconds")
