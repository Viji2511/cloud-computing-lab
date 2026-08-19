import time
coordinator=0
queue=[1,2,3]
print("coordinator is process",coordinator)
for process in queue:
    print(f"\nProcess {process} requests critical section")
    time.sleep(1)
    print("Coordinatot grants permission")
    time.sleep(1)
    print(f"Process {process} enters critical section")
    time.sleep(2)
    print(f"Process {process} exits critical section")
    print("Coordinator released critical section")