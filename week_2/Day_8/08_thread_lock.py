# In such programs, Python’s GIL was known to starve the I/O-bound threads by not giving them a chance to acquire the GIL from CPU-bound threads.
# This was because of a mechanism built into Python that forced threads to release the GIL after a fixed interval of continuous use 
# and if nobody else acquired the GIL, the same thread could continue its use.

import threading 

counter =0
lock =threading.Lock()

def increment():
    global counter 
    for _ in range(100000):
        with lock:
            counter += 1

threads =[ threading.Thread(target=increment) for _ in range(10)]
[t.start() for t in threads]
[t.join() for t in threads]

print(f" Final counter value: {counter}")