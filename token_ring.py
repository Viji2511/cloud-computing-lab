import time
processes=[1,2,3,4]
token=0
for i in range(8):
    print(f"\nToken with process {processes[token]}")
    print(f"Process {processes[token]} enters critical section")
    time.sleep(1)
    print(f"Process {processes[token]} exits critical section")
    token=(token+1)%len(processes)