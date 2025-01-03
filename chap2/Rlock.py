import threading
import time
import random

class Box:
    def __init__(self):
        # Create a reentrant lock (RLock)
        self.lock = threading.RLock()  
        self.total_items = 0  # Initial total_items is 0

    def execute(self, value):
        with self.lock:  # Acquiring the lock
            self.total_items += value  # Modifying shared resource (total_items)

    def add(self):
        with self.lock:  # Acquiring the lock
            self.execute(1)  # Increase the total_items by 1

    def remove(self):
        with self.lock:  # Acquiring the lock
            self.execute(-1)  # Decrease the total_items by 1

def adder(box, items):
    print("N° {} items to ADD \n".format(items))
    while items:  # While there are items to add
        box.add()  # Add one item to the box (this calls Box.add() method)
        time.sleep(1)  # Sleep for 1 second to simulate some delay
        items -= 1  # Decrement the number of items to add
        print("ADDED one item -->{} item to ADD \n".format(items))

def remover(box, items):
    print("N° {} items to REMOVE \n".format(items))
    while items:  # While there are items to remove
        box.remove()  # Remove one item from the box (this calls Box.remove() method)
        time.sleep(1)  # Sleep for 1 second to simulate some delay
        items -= 1  # Decrement the number of items to remove
        print("REMOVED one item -->{} item to REMOVE\n".format(items))

def main():
    items = 10  # This is the initial number of items in the box
    box = Box()  # Create an instance of the Box class

    # Create two threads: one for adding items and one for removing items
    t1 = threading.Thread(target=adder, args=(box, random.randint(10,20)))  # Adder thread with random items to add
    t2 = threading.Thread(target=remover, args=(box, random.randint(1,10)))  # Remover thread with random items to remove

    # Start the threads
    t1.start()
    t2.start()

    # Wait for both threads to finish before continuing
    t1.join()
    t2.join()

if __name__ == "__main__":
    main()