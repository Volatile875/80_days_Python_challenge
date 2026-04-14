# btw you can bypass the mutex lock by using multiprocessing instead of threading.

from multiprocessing import Process
import time

def crunch_number():
    print(f"Starred the count process..")
    count = 0
    for _ in range(100_00_00):
        count += 1
    print(f"Ended the count process..: {count}")

start = time.time()

if __name__=="__main__":
    start = time.time()

    p1= Process(target=crunch_number)
    p2= Process(target=crunch_number)

    p1.start()
    p2.start()
    p1.join()
    p2.join()

    end= time.time()

    print(f"Total time with multiprocessing: {end-start:.2f} seconds")