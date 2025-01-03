import threading
import time  # Importing time to measure execution time

def calc_fibonacci(n):
    if n == 0 or n == 1:
        return n 
    return calc_fibonacci(n-1) + calc_fibonacci(n-2)

threads = []

# Start the timer before thread execution
start_time = time.time()

for i in range(4):
    t = threading.Thread(target=calc_fibonacci, args=(30,))
    threads.append(t)
    print(f"Starting thread {i+1}")
    t.start()

# Join all threads after starting them
for t in threads:
    t.join()


end_time = time.time()


execution_time = end_time - start_time
print("All threads have finished.")
print(f"Total execution time: {execution_time:.4f} seconds")