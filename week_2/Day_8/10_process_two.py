from multiprocessing import Process
import time

def cpu_heavy():
    print(f"Crunching some numbers...")
    total = 0
    for i in range(10**9):
        total += i
    print(f" DONE ")

start =time.time()

if __name__=="__main__":
    start=time.time()

    Process= [Process(target=cpu_heavy) for _ in range(2)]

    [t.start() for t in Process]
    [t.join() for t in Process]  
    

    end=time.time()

    print(f" Total: {end-start:.2f} seconds")