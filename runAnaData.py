#!/usr/bin/env python
# -*- coding: utf-8 -*-  
# by zhangzhi @2013-10-13 21:24:20 
# Copyright 2013 NONE rights reserved.

import Process

def calMean(dataDict):
    "count MEAN"
    if len(dataDict) == 0:
        return None
    return float(sum(dataDict.values())) / len(dataDict)

def calMeadian(dataDict):
    "count MEADIAN"
    if len(dataDict) == 0:
        return None
    return sorted(dataDict.values())[len(dataDict)/2]

"""
count Standard Deviation
"""
def calStdDeviation(dataDict):
    import math
    if len(dataDict) == 0:
        return 0
       
    mean = calMean(dataDict)
    var = 0.0
    for data in dataDict.values():
        var += (data - mean) ** 2    
    stdDeva = math.sqrt(var)
    return stdDeva

"""
select data
"""
def selectData(dataList):
    dataDict = {}
    for data in dataList:
        if data[0] not in dataDict:
            dataDict[data[0]] = data[3]
    return dataDict

if __name__ == '__main__':
    dataDict = {}
    dataList = Process.process('data1')
    dataDict = selectData(dataList)      
    print 'calMean(dataDict)'
    print "%.5f" % calMean(dataDict) 
    print 'calMeadian(dataDict)'
    print "%.5f" % calMeadian(dataDict) 
    print 'calStdDeviation(dataDict)'
    print "%.5f" % calStdDeviation(dataDict) 


