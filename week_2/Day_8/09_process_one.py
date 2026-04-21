# Basically in this particular code we are going to learn about
# how the processes or mutil- porcessing works with Queue and Values.

import threading
import time

def cpu_heavy():
    print(f"Crunching some numbers...")
    total = 0
    for i in range(10**9):
        total += i
    print(f" DONE ")

start =time.time()

threads= [threading.Thread(target=cpu_heavy) for _ in range(2)]

[t.start() for t in threads]
[t.join() for t in threads]  
 

end=time.time()

print(f" Total: {end-start:.2f} seconds")