import multiprocessing
import random
import time

class producer(multiprocessing.Process):
   def __init__(self, queue):
       multiprocessing.Process.__init__(self)
       self.queue = queue
  
   def run(self):
       for i in range(10):
           item = random.randint(0, 256)
           self.queue.put(item)  # Add item to the queue
           print(f"Process Producer: item {item} appended to queue {self.name}")
           time.sleep(1)
           print(f"The size of queue is {self.queue.qsize()}")
      
       # After producing all items, put a sentinel value to stop the consumer
       self.queue.put(None)
      
class consumer(multiprocessing.Process):
   def __init__(self, queue):
       multiprocessing.Process.__init__(self)
       self.queue = queue

   def run(self):
       while True:
           item = self.queue.get()  # Get item from the queue
           if item is None:
               print("Consumer: No more items to process. Exiting.")
               break
           print(f"Process Consumer: item {item} popped by {self.name}")
           time.sleep(2)

if __name__ == '__main__':
   queue = multiprocessing.Queue()
  
   # Create producer and consumer processes
   process_producer = producer(queue)
   process_consumer = consumer(queue)
  
   # Start the producer and consumer processes
   process_producer.start()
   process_consumer.start()
  
   # Wait for the processes to finish
   process_producer.join()
   process_consumer.join()

