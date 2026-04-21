import threading
import time

def background_task():
    while True:
        print("Daemon thread running...")
        time.sleep(1)

# Create a daemon thread
t = threading.Thread(target=background_task, daemon=True)
t.start()

print("Main thread will sleep for 3 seconds...")
time.sleep(3)
print("Main thread exiting. Daemon thread will be killed automatically.")
