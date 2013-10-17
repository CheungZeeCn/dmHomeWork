#!/usr/bin/env python
# -*- coding: utf-8 -*-  
# by zhangzhi @2013-10-13 22:02:25 
# Copyright 2013 NONE rights reserved.

import math

g_cDict = {'C1':[1.8, 2.3], 'C2':[4.1, 5.4]}
g_pDict = {
            'P1':{'coordinates':(1.0, 1.0), 'cluster':None},  
            'P2':{'coordinates':(1.5, 2.0), 'cluster':None},  
            'P3':{'coordinates':(3.0, 4.0), 'cluster':None},  
            'P4':{'coordinates':(5.0, 7.0), 'cluster':None},  
            'P5':{'coordinates':(3.5, 5.0), 'cluster':None},  
            'P6':{'coordinates':(4.5, 5.0), 'cluster':None},  
            'P7':{'coordinates':(3.5, 4.5), 'cluster':None},  
}

def showPoints(pDict): 
    filedFormat = "| %10s | %15s | %8s |"
    print ' ' + '-' * 41 + ' '
    print filedFormat % ('point', 'coordinates', 'cluster')
    for each in sorted(pDict.keys()):
        print filedFormat % (each, pDict[each]['coordinates'], pDict[each]['cluster'])      
    print ' ' + '-' * 41 + ' '

def showCluster(cDict):
    filedFormat = '| %8s | %15s |' 
    print ' ' + '-' * 28 + ' '
    print filedFormat % ('cluster', 'coordinates')
    for each in sorted(cDict.keys()):
        print filedFormat % (each, cDict[each])      
    print ' ' + '-' * 28 + ' '

def dist(p1, p2):
    dSum = 0
    for i in range(len(p1)):
        dSum += (p1[i] - p2[i]) ** 2
    return math.sqrt(dSum)

def reCenter(pDict, div=2):
    global g_cDict
    cDict = {} 
    cDictCnt = {}
    for p in pDict:
        c = pDict[p]['cluster']    
        if c not in cDict:
            cDict[c] = [0] * div
            cDictCnt[c] = 0
        for d in range(len(pDict[p]['coordinates'])):
            cDict[c][d] += pDict[p]['coordinates'][d]    
        cDictCnt[c] += 1
    
    for c in cDict:
        for d in range(len(cDict[c])):
            cDict[c][d] /= cDictCnt[c]
    
    g_cDict = cDict
    return True

def assignPoints():
    global g_cDict, g_pDict 
    flagChanged = False
    for p in g_pDict:
        minC = None
        minDist = None
        for c in g_cDict:
            theDist = dist(g_pDict[p]['coordinates'], g_cDict[c])
            if minC == None:
                minC = c
                minDist = theDist
            elif theDist <= minDist:
                minC = c
                minDist = theDist
        if g_pDict[p]['cluster'] != minC:
            flagChanged = True
        g_pDict[p]['cluster'] = minC                       
    return flagChanged

def show():
    showPoints(g_pDict)
    showCluster(g_cDict)

def kmeansRun():
    global g_cDict, g_pDict
    while assignPoints() == True:
        reCenter(g_pDict, 2) 
        show()

if __name__ == '__main__':
    show()
    kmeansRun()


