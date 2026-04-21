from multiprocessing import Process
import time

def brew_chai(name):
    print(f" Stating making chai {name} chai brewing")
    time.sleep(3)
    print(f"Ending making chai {name} chai brewing")

if __name__=="__main__":
    chai_makers = [
        Process(target=brew_chai, args=(f"Chai Maker #{i+1}",))
        for i in range(3)
    ]
    
    #starting all prcesses:
    for p in chai_makers:
        p.start()

    # wait for all too complete
    for p in chai_makers:
        p.join()

    print("All chai are served")

    
         