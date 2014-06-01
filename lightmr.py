#!/usr/bin/env python
#coding: utf8

from multiprocessing import Pool

def f(x):
    return x**2

def callback(x):
    print(x)

def main():
    pool = Pool(processes=1)
    result = pool.apply_async(f, [10], callback)

if __func__ == '__main__':
    main()
