![ALT TEXT](images/code1.png)
![ALT TEXT](images/code2.png)
![ALT TEXT](images/code3.png)
![ALT TEXT](images/code4.png)
![ALT TEXT](images/code5.png)


# Chapter 4: Message Passing

This chapter focuses on demonstrating message-passing techniques using **MPI (Message Passing Interface)** with the **mpi4py** library in Python. The examples in this chapter showcase how to manage communication between multiple processes in a parallel computing environment. Key concepts include sending and receiving data between processes, using collective communication, and understanding Cartesian topology for process communication.

## Contents

### 1. **basic_mpi_example.py**
This script demonstrates basic **MPI** communication using the **mpi4py** library. It covers the following concepts:
- **Initializing MPI**: Set up the MPI environment and initialize the processes.
- **Sending and Receiving Data**: Sending and receiving data between different processes using `send` and `recv`.
- **Process Ranks and Sizes**: How processes are assigned ranks and sizes, and how to handle different ranks in communication.

### 2. **collective_communication.py**
This example illustrates the use of **collective communication** in MPI. It uses the `gather` function to collect data from all processes and send it to the root process. This technique is useful when you need to collect data from multiple parallel processes and process it in a central location.

#### Key Points:
- **Using `gather` to collect data**: How to gather data from all processes and send it to the root process.
- **Root Process Handling**: How the root process handles the collected data.

### 3. **cartesian_topology_example.py**
This script demonstrates the use of **Cartesian topology** for process communication in a 2D grid. It uses MPI's `Create_cart` method to create a grid of processes and illustrates how to send data between neighboring processes in the grid.

#### Key Points:
- **Creating a 2D Grid of Processes**: Using MPI’s `Create_cart` to create a Cartesian grid of processes.
- **Using `Shift` for Neighbor Communication**: How to use the `Shift` function to communicate with neighboring processes in the grid.

## Requirements

To run the scripts in this chapter, you need to install the **mpi4py** library. This library allows you to perform message-passing communication between processes.

### Required Libraries:
- `mpi4py`: Library for MPI-based communication.

### Installation Instructions:
To install the necessary library, use the following command:

```bash
pip install mpi4py
