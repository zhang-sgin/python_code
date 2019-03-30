from concurrent.futures import ThreadPoolExecutor
import time


def task(host):
    time.sleep(2)
    print(host)


pool = ThreadPoolExecutor(20)

for i in range(1, 101):
    host_name = "c{}.com".format(i)
    
    pool.submit(task, host_name)
