import time
processes=[1,2,3]
for process in processes:
    print(f"\nProcess {process} requests critical section")
    time.sleep(1)
    print("sending REQUEST messages..")
    time.sleep(1)
    print("receiving REPLY messages..")
    time.sleep(1)
    print(f"Process {process} enters critical section")
    time.sleep(2)
    print(f"Process {process} exits critical section")
