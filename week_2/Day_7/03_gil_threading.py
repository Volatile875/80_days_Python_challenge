# suppose you have two seperate threads and in both thread you are executing to chnage a praticular value 
# and if both the threads are trying to change the same value at the same time then question arises that
# which thread will get the access to change the value first and which thread will get the access to change
# the value second and this is where GIL comes into picture and the mutex lock is used to solve this problem 
# and the GIL is a mutex lock that protects access to Python objects,
# preventing multiple threads from executing Python bytecode simultaneously.
# This means that even if you have multiple threads in your Python program,
# only one thread can execute Python code at a time. The GIL is necessary because CPython's memory management 
# is not thread-safe, and it ensures that only one thread can access Python objects at a time, preventing.


import threading
import time

def brew_chai():
    print(f" {threading.current_thread().name} is starting to brew chai")
    count = 0
    for _ in range(5):
        count += 1
        print(f"{threading.current_thread().name} finishing brewing..: {count}")\
        
thread1 = threading.Thread(target=brew_chai, name=" BARISTA-1")
thread2= threading.Thread(target= brew_chai, name=" BARISTA-2")

start= time.time()
thread1.start()
thread2.start() 
thread1.join()
thread2.join()
end = time.time()  

print(f"Total time taken: {end-start:.2f} seconds")