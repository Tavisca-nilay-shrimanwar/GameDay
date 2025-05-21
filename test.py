import time

for i in range(5):
    print(i)
    time.sleep(1)

raise Exception("something went wrong")
