#!/usr/bin/env python
# -*- coding: utf-8 -*-  
# by zhangzhi @2013-10-13 16:20:48 
# Copyright 2013 NONE rights reserved.

import ReadUtil


def isInt(peer):
    val = None
    try:
        val = int(peer)
    except Exception, e:
        return False
    return True

def isStudentId(peer):
    if isInt(peer):
        if len(peer) <= 30:
            return True
        else:
            return False
    else:
        return False
        
def preStudentId(peer):
    if isStudentId(peer):
        return peer
    else:
        return None 

def preName(peer):
    if len(peer) <= 30:
        return  peer  
    else:
        return  None

def preGender(peer):
    if peer.lower() != 'male' and \
        peer.lower() != 'female':
            return 'other'
    else:
        return peer.lower()   

def preGPA(peer):
    try: 
        gpa = float(peer)
    except Exception, e:
        return None
    if gpa <= 0 or gpa > 5:
        return None
    else:
        return gpa

def preCS(peer):
    if peer.lower() == 'yes':
        return True
    elif peer.lower() == 'no':
        return False
    else:
        return None

def preCourse(peer):
    if len(peer) >= 50:
        return None
    else:
        return peer.lower()

def _process(dataList):
    ret = []
    error = 0
    for each in dataList:
        try:
            each = [ preStudentId(each[0]), preName(each[1]), preGender(each[2]), \
                    preGPA(each[3]), preCS(each[4]), preCourse(each[5]) ]   
        except Exception, e:
            error += 1
            continue
        if each[0] == None:
            error += 1
            continue
        else:
            ret.append(each)
    return ret

def process(fileName):
    ret = ReadUtil.readRawFileData(fileName)    
    ret = _process(ret)
    return ret

if __name__ == '__main__':
    print 'hello world'

