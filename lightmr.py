#!/usr/bin/env python
#coding: utf8

# NOTE: each machine is either client or server.
# 1. Client broadcast to all machines which have installed lightmr.
# // 2. Each machine report its resource to the client.
# 3. Client set the plan and distribute it to all servers.


# Role: controller, client, server
#   Controller may be an optional role, because if we know all the ip,
#   then it's not so important..
LIGHTMR_CONTROLLER = 'www.anwcl.com'


# Controller: store all avaiable computing nodes' ip,
#   and manage them to run tasks.
computing_resource_list = list()

def sync_computing_resource():
    pass

def join_lightmr_group():
    pass

def leave_lightmr_group():
    pass

def update_to_newest_version():
    pass

# No controller test.
ip_list = ["192.168.1.21", "192.168.1.22"]


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
    pool = Pool(processes=3)
    for i in range(10):
        result = pool.apply_async(f, args=(i, ), callback=callback)
    pool.close()
    pool.join()
    print(result_list)

if __name__ == '__main__':
    main()
