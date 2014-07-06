#!/usr/bin/env python
#coding: utf8

# NOTE: each machine is either client or server.
# 1. Client broadcast to all machines which have installed lightmr.
# // 2. Each machine report its resource to the client.
# 3. Client set the plan and distribute it to all servers.

# remote map
def map(func, data):
    # send request meta-data to all machines
    # send part of data to all machines
    # and let them start to process data use a function
    return 0

def reduce():
    return 0

# local map-reduce example
from multiprocessing import Pool
import time

def f(x):
    return x**2

result_list = []
def callback(result):
    result_list.append(result)
    # with open("test.log") as test_file:
    #     test_file.write(x)

def main():
    pool = Pool(processes=1)
    for i in range(10):
        result = pool.apply_async(f, args=(i, ), callback=callback)
    pool.close()
    pool.join()
    print(result_list)

if __name__ == '__main__':
    main()
