#!/usr/bin/env python
# -*- coding: utf-8 -*-  
# by zhangzhi @2013-10-14 00:31:18 
# Copyright 2013 NONE rights reserved.


import math

g_pDict = {
            'P1':(3, 4),  
            'P2':(3, 3),  
            'P3':(6, 2),  
            'P4':(10, 12),  
            'P5':(11, 11),  
            'P6':(12, 10),  
        }

g_cDict = {
            'P1':[(3, 4)],  
            'P2':[(3, 3)],  
            'P3':[(6, 2)],  
            'P4':[(10, 12)],  
            'P5':[(11, 11)],  
            'P6':[(12, 10)],  
        }

def showCluster(cDict):
    filedFormat = '| %8s | %15s |' 
    print ' ' + '-' * 28 + ' '
    print filedFormat % ('cluster', 'coordinates')
    for each in sorted(cDict.keys()):
        print filedFormat % (each, cDict[each])      
    print ' ' + '-' * 28 + ' '

def pDistEuc(p1, p2):
    dSum = 0
    for i in range(len(p1)):
        dSum += (p1[i] - p2[i]) ** 2
    return math.sqrt(dSum)

def cDistComplete(c1L, c2L):
    maxLength = 0
    for eachC1 in c1L:
        for eachC2 in c2L:
            theDist = pDistEuc(eachC1, eachC2)
            if theDist > maxLength:
                maxLength = theDist
    return maxLength

def cDistSingle(c1L, c2L):
    minLength = None
    for eachC1 in c1L:
        for eachC2 in c2L:
            theDist = pDistEuc(eachC1, eachC2)
            if minLength == None or theDist < minLength:
                minLength = theDist
    return minLength

def addPoint(l1, l2):
    ret = []
    for i in range(len(l1)):
        ret.append(l1[i] + l2[i])
    return ret

def cDistCentroid(c1L, c2L):
    print c1L, c2L
    c1 = reduce(addPoint, c1L)
    l = len(c1L)
    c1 = [ each/l for each in c1 ]
    c2 = reduce(addPoint, c2L)
    l = len(c2L)
    c2 = [ each/l for each in c2 ]
    print "c1: %s |c2: %s" % (c1, c2)
    return pDistEuc(c1, c2)

def calCMeadian(cL):
    c = []
    d = len(cL[0])
    l = len(cL)
    for di in range(d):
        c.append(sorted([ p[di] for p in cL])[l/2])
    return c
                
def cDistMeadian(c1L, c2L):
    print c1L, c2L
    c1 = calCMeadian(c1L) 
    c2 = calCMeadian(c2L) 
    print "c1: %s |c2: %s" % (c1, c2)
    return pDistEuc(c1, c2)

def cDistGA(c1L, c2L):
    sumLength = 0.0
    n = 0
    for eachC1 in c1L:
        for eachC2 in c2L:
            theDist = pDistEuc(eachC1, eachC2)
            theDist2 = pDistEuc(eachC2, eachC1)
            sumLength += (theDist + theDist2)
            n += 2
    if n == 0:
        return 0
    return sumLength/n

def showDistMatrix(distM):
    d = len(distM)
    fields = d + 1 
    fieldWidth = 10
    keys = sorted(distM.keys())
    #"print header"    
    print ' ' + '-' * ((fieldWidth + 3) * fields + -1)
    print ("|" + ( " %%%ds |" % fieldWidth) * fields) % tuple(['DIST'] + keys)
    for p1 in keys:
         print ("|" + (" %%%ds |" % fieldWidth) * fields) % \
                tuple([p1] + [ "%.5f" % distM[p1][p2] for p2 in keys ])
    print ' ' + '-' * ((fieldWidth + 3) * fields + -1)

def mergeClusterDistMatrix(distFunc):
    global g_pDict
    distMatrix = {}
    for p1 in g_cDict:
        if p1 not in distMatrix:   
            distMatrix[p1] = {}
        for p2 in g_cDict:
            theDist = distFunc(g_cDict[p1], g_cDict[p2])
            distMatrix[p1][p2] = theDist
    return distMatrix

def merger2Cluster(c1, c2):
    global g_cDict
    c1L = g_cDict[c1]
    c2L = g_cDict[c2]
    c1c2L = c1L + c2L
    del g_cDict[c1]
    del g_cDict[c2]
    g_cDict[c1+c2] = c1c2L

def clustering(cDistFunc):
    global g_cDict
    while len(g_cDict.keys()) != 1:
        cDistMatrix = {}
        peerPair = None
        peerDist = None
        keys = sorted(g_cDict.keys())
        cTmp = None
        #iter
        for c1 in keys:
            if c1 not in cDistMatrix:
                cDistMatrix[c1] = {}
            for c2 in keys:    
                if c2 not in cDistMatrix:
                    cDistMatrix[c2] = {}
                if c2 == c1:
                    cDistMatrix[c1][c2] = 0
                    cTmp = c2
                    break
                #calDist
                dist = cDistFunc(g_cDict[c1], g_cDict[c2])
                cDistMatrix[c1][c2] = dist
                cDistMatrix[c2][c1] = dist
                if peerPair == None or peerDist >= dist:
                    peerPair = [c1, c2]
                    peerDist = dist
            if cTmp == c1:
                continue
        #merge
        showDistMatrix(cDistMatrix)
        merger2Cluster(peerPair[0], peerPair[1])
    
def calPointDistMatrix(distFunc):
    global g_pDict
    distMatrix = {}
    for p1 in g_pDict:
        if p1 not in distMatrix:   
            distMatrix[p1] = {}
        for p2 in g_pDict:
            theDist = distFunc(g_pDict[p1], g_pDict[p2])
            distMatrix[p1][p2] = theDist
    return distMatrix

if __name__ == '__main__':
    global g_cDict
    import sys
    import copy
    g_cDictDump = copy.deepcopy(g_cDict)
    pDistM = calPointDistMatrix(pDistEuc)
    showDistMatrix(pDistM) 
    print "=" * 40 + 'complete clustering begin' + "=" * 40
    clustering(cDistComplete)
    print "=" * 40 + 'clustering end' + "=" * 40
    g_cDict = copy.deepcopy(g_cDictDump)
    print "=" * 40 + 'single clustering begin' + "=" * 40
    clustering(cDistSingle)
    print "=" * 40 + 'clustering end' + "=" * 40

    
    print "=" * 40 + 'GA clustering begin' + "=" * 40
    g_cDict = {'P1P2P3': [ g_pDict[x] for x in ('P1','P2','P3') ], \
               'P4P5P6': [ g_pDict[x] for x in ('P4','P5','P6') ],}
    clustering(cDistGA)
    print "=" * 40 + 'GA clustering end' + "=" * 40

    print "=" * 40 + 'CenTroid clustering begin' + "=" * 40
    g_cDict = {'P1P2P3': [ g_pDict[x] for x in ('P1','P2','P3') ], \
               'P4P5P6': [ g_pDict[x] for x in ('P4','P5','P6') ],}
    clustering(cDistCentroid)
    print "=" * 40 + 'CenTroid clustering end' + "=" * 40

    print "=" * 40 + 'Median clustering begin' + "=" * 40
    g_cDict = {'P1P2P3': [ g_pDict[x] for x in ('P1','P2','P3') ], \
               'P4P5P6': [ g_pDict[x] for x in ('P4','P5','P6') ],}
    clustering(cDistMeadian)
    print "=" * 40 + 'Medianclustering end' + "=" * 40

