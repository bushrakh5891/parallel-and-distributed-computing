from concurrent.futures import ThreadPoolExecutor

# Define the tasks
def task_1():
    print("Task 1 executed")

def task_2():
    print("Task 2 executed")

# Use ThreadPoolExecutor to execute tasks
with ThreadPoolExecutor() as executor:
    future1 = executor.submit(task_1)  # Schedule task_1
    future2 = executor.submit(task_2)  # Schedule task_2