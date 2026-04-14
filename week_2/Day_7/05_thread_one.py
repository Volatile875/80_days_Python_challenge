# threads and lock in deepth technique:

import threading
import time

def boil_milk():
    print(f"Boling the milk...")
    time.sleep(2)
    print(f"done with boiling the milk...")

def toast_bun():
    print(f"Toasting the bun...")
    time.sleep(3)
    print(f"done with toasting the bun...")

start = time.time()

t1= threading.Thread(target=boil_milk)
t2= threading.Thread(target=toast_bun)

t1.start()
t2.start()
t1.join()
t2.join()

end= time.time()
print(f" total time taken: {end - start:.2f} seconds")
