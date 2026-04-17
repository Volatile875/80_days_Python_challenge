import threading

lock_a= threading.Lock()
lock_b=threading.Lock()

def task1():
    with lock_a:
        print("Taks 1 acquired lock a...")
        with lock_b:
            print("Task aquired lock b...")

def task2():
    with lock_b:
        print("Taks 1 acquired lock a...")
        with lock_a:
            print("Task2 aquired lock b...")

thread1= threading.Thread(target=task1)
thread2= threading.Thread(target=task2)

thread1.start()
thread2.start()


