#!/usr/bin/env python
#coding: utf8

# NOTE: each machine is either client or server.
# 1. Client broadcast to all machines which have installed lightmr.
# // 2. Each machine report its resource to the client.
# 3. Client set the plan and distribute it to all servers.


import asyncore
import socket


class EchoHandler(asyncore.dispatcher_with_send):

    def handle_read(self):
        data = self.recv(8192)
        print('recv: ' + data)
        try:
            exec(data)
        except Exception as e:
            print('Exception:' + str(e))
        if data:
            self.send(data)
            print('send: ' + data)

class EchoServer(asyncore.dispatcher):

    def __init__(self, host, port):
        asyncore.dispatcher.__init__(self)
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        self.set_reuse_addr()
        self.bind((host, port))
        self.listen(5)

    def handle_accept(self):
        pair = self.accept()
        if pair is not None:
            sock, addr = pair
            print 'Incoming connection from %s' % repr(addr)
            handler = EchoHandler(sock)

server = EchoServer('localhost', 8090)
asyncore.loop()


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

# Client
def send_cmd(ip, func, data):
    print('send cmd '+func+' to '+ip)
    return

# Server
def response_cmd(ip, func, data):
    pass

# remote map to all machines in the cluster.
def map(func, data):
    # send request meta-data to all machines
    # send part of data to all machines
    # and let them start to process data use a function

    for ip in ip_list:
        send_cmd(ip, func, data)

    return 0

# collect data from the response.
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


def process_pool_test():
    print('process_pool_test')
    pool = Pool(processes=3)
    for i in range(10):
        result = pool.apply_async(f, args=(i, ), callback=callback)
    pool.close()
    pool.join()
    print(result_list)

def map_test():
    print('map_test')
    return

def main():
    process_pool_test()
    map_test()

if __name__ == '__main__':
    main()
