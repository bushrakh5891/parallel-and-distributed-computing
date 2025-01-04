Chapter 1: Introduction to Parallel Computing
This folder contains code examples and exercises related to Chapter 1: Introduction to Parallel Computing. In this chapter, the key concepts of parallel computing are introduced, including basic parallelism models, multithreading, and how parallel computing can speed up processes.

The examples here demonstrate simple parallel computing techniques and their applications.

Table of Contents
Overview
Code Examples
Example 1: Parallel Sorting
Example 2: Parallel Matrix Multiplication
Setup Instructions
Usage
Contributing
License
Overview
In Chapter 1, we cover the fundamentals of parallel computing, including the following topics:

Introduction to Parallel Computing
Parallelism Models (data parallelism, task parallelism)
Threads and Multithreading
Basic Applications of Parallel Computing (sorting, matrix multiplication)
These concepts are demonstrated through basic Python examples and multithreading techniques.

Code Examples
Example 1: Parallel Sorting
In this example, the sorting algorithm is parallelized using Python's threading module. The code splits the list into smaller chunks, sorts each chunk in parallel, and then combines the sorted chunks.

How it works:
The input list is divided into several sublists.
Each sublist is sorted in parallel by different threads.
Finally, the sorted sublists are merged together.
Example Usage:

bash
Copy code
cd chap1
python3 parallel_sorting.py
Example 2: Parallel Matrix Multiplication
This example demonstrates the use of parallel computing for matrix multiplication. The task is divided into smaller tasks (multiplying parts of the matrices), which are processed in parallel to speed up the overall computation.

How it works:
The input matrices are split into smaller submatrices.
Each submatrix multiplication is done in parallel.
The final result is obtained by combining the results from each parallel task.
