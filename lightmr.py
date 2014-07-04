#!/usr/bin/env python
#coding: utf8

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
