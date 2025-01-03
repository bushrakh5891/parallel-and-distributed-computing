from multiprocessing import Process

def print_square(num):
    print(f"Square: {num * num}")

def print_cube(num):
    print(f"Cube: {num * num * num}")

if __name__ == '__main__':
    p1 = Process(target=print_square, args=(10,))
    p2 = Process(target=print_cube, args=(10,))
    
    p1.start()
    p2.start()
    
    p2.join()  # Wait for p2 to finish before proceeding
    p1.join()  # Wait for p1 to finish before proceeding
    
    print("Processes finished executing")