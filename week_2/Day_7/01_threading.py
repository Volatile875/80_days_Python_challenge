# Work of ( 9th april 2026)

import threading
import time

def take_order():
    for i in range(1, 4):
        print(f"taking order {i}")
        time.sleep(2)

def brew_coffee():
    for i in range(1, 4):
        print(f"brewing coffee process {i} \n")
        time.sleep(3)

#creating  threads
order_thread = threading.Thread(target=take_order)
brew_thread = threading. Thread(target=brew_coffee)

order_thread.start()
brew_thread.start()

# wait for both threads to finish
order_thread.join()
brew_thread.join()