#!/usr/bin/env python
# -*- coding: utf-8 -*-  
# by zhangzhi @2013-10-13 20:58:40 
# Copyright 2013 NONE rights reserved.

import ReadUtil as R

def doReduce(l):
    return reduce(add, l)

def add(l1, l2):
    ret = []
    for i in range(len(l1)):
        ret.append(l1[i] + l2[i])        
    return ret

if __name__ == '__main__':
    print doReduce(((1,2,3), (4,5,6), (4,3,2)))

