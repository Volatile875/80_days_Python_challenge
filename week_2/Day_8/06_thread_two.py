import threading 
import time

def prepare_chai(type, wait_time):
    print(f"{type} chai: brewing...")
    time.sleep(wait_time)
    print(f"{type} chai: Ready!")

t1 = threading.Thread(target= prepare_chai, args=("Masala", 2))
t2 = threading.Thread(target= prepare_chai, args=("Ginger", 3))

t1.start()
t2.start()
t1.join()
t2.join()
print("All chai is ready! Enjoy your tea time!")