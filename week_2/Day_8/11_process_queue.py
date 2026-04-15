from multiprocessing import Process, Queue
import time

def prepare_dish(queue):
    queue.put(f"Preparing a masala chai...")

if __name__=="__main__":
    queue = Queue()

    
    p1= Process(target=prepare_dish, args=(queue,))
    p1.start()
    p1.join()

    print(queue.get())