# parallel-and-distributed-computing
# Basic Python Codes

This repository contains basic Python programs designed to demonstrate fundamental programming concepts and advanced techniques like parallel computing, threading, multiprocessing, and GPU computing. Each file highlights specific concepts and functionalities relevant to beginner and intermediate Python programmers.

## Contents

### 1. **calculator.py**
A simple calculator program that performs basic arithmetic operations (addition, subtraction, multiplication, and division). Users can input two numbers and choose the desired operation.

### 2. **data_structures.py**
This file demonstrates the use of various data structures in Python, including:
- Tuples
- Lists
- Dictionaries

Examples and explanations are provided to help understand how to use these data structures effectively.

### 3. **functions.py**
This script showcases how to define and use functions in Python. It includes examples of:
- Defining functions
- Function parameters and return values
- Calling functions

### 4. **classes.py**
This file introduces object-oriented programming (OOP) in Python. It covers:
- Creating classes and objects
- Defining methods
- Using inheritance

### 5. **mpi_example.py**
This script demonstrates how to use **MPI** (Message Passing Interface) for distributed computing with **mpi4py**. It shows basic communication between processes:
- Sending and receiving data using MPI
- Handling process ranks and sizes

### 6. **multiprocessing_vs_threading.py**
This script compares multiprocessing and threading for concurrent programming:
- **Multiprocessing**: Using Python’s `multiprocessing` module to spawn multiple processes.
- **Multithreading**: Using Python’s `threading` module to spawn multiple threads.

It measures and compares execution times for both techniques using a basic list processing task.

### 7. **gpu_computation.py**
Demonstrates how to leverage **GPU** for parallel computing using **Numba**'s CUDA JIT compiler:
- Vector addition using GPU for accelerated computation
- Verifying the result using Numba’s CUDA capabilities.

### 8. **num_parallel_computing.py**
This script demonstrates vector addition using data parallelism with **NumPy**:
- Simple vector addition to compute the result using NumPy's optimized parallelism.
- Measures and prints execution time for large vector sizes.

### 9. **threadpool_executor.py**
Illustrates the use of **ThreadPoolExecutor** to manage a pool of threads for concurrent execution of tasks:
- Demonstrates executing multiple tasks in parallel with a thread pool.
- Uses `ThreadPoolExecutor` to run functions asynchronously.

### 10. **producer_consumer.py**
This script demonstrates the producer-consumer problem using **multiprocessing**:
- Two processes, `producer` and `consumer`, communicate via a `Queue`.
- The producer produces items and the consumer consumes them.

### 11. **semaphore_example.py**
This script demonstrates how to use a **semaphore** to control access to a shared resource with threading:
- Controls access to a resource by limiting the number of concurrent threads that can access it.

### 12. **multiprocessing_example.py**
Demonstrates **multiprocessing** with basic process spawning:
- Executes two functions (print square and print cube) in parallel using separate processes.
- Shows process synchronization and joining.

### 13. **fibonacci_threading.py**
Illustrates using multiple threads to calculate Fibonacci numbers:
- Uses **threading** to calculate Fibonacci numbers concurrently.

### 14. **threading_event_example.py**
Demonstrates **threading events** for communication between threads:
- Producer creates random numbers, and consumer consumes them using an event to synchronize operations.

### 15. **lock_example.py**
Shows how to use **thread locks** for synchronization in multithreading:
- Locks prevent race conditions by ensuring only one thread can access a shared resource at a time.

## Requirements

To run these scripts, you need Python 3.x and some external libraries:
- `mpi4py` for MPI examples
- `numba` and `numpy` for GPU computing examples
- `concurrent.futures` for ThreadPoolExecutor
- `multiprocessing` and `threading` for concurrent and parallel programming examples

You can install the required libraries using:

```bash
pip install mpi4py numba numpy
