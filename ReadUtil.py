#!/usr/bin/env python
# -*- coding: utf-8 -*-  
# by zhangzhi @2013-10-06 11:43:07 
# Copyright 2013 NONE rights reserved.

import sys
import re

def readRawFileData(fileLoc, d=' '):
    lineList = []
    with open(fileLoc) as f:
        for each in f:
            ret = each.strip().split(d)
            lineList.append(ret)   
    return lineList

def readRawFileData_reSplit(fileLoc, d=r'\s+'):
    lineList = []
    reSplt = re.compile(d)
    with open(fileLoc) as f:
        for each in f:
            ret = reSplt.split(each.strip())
            lineList.append(ret)   
    return lineList

if __name__ == '__main__':
    print readRawFileData("data1")

