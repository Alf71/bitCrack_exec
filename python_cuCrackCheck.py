#!/usr/bin/evn python
# -*- coding: utf-8 -*-
#2015-03-05

import  os
import  sys
import  copy
import  time
import  string
import  random 
import  socket
import thread  

import win32com.client
 
def CheckProcExistByPN(process_name):
    try:
        WMI = win32com.client.GetObject('winmgmts:') 
        processCodeCov = WMI.ExecQuery('select * from Win32_Process where Name="%s"' % process_name)
    except Exception,e:
        print process_name + "error : ", e;
    if len(processCodeCov) > 0:
        print process_name + " exist";
        return False
    else:
        print process_name + " is not exist";
        return True
  
if __name__ == '__main__':
    lCnt = 0
    retValue = False
    while 1:
        CheckProcExistByPN('cuBitCrack.exe')
        if (retValue == False):
            os.system('cuBitCrack.bat')
        time.sleep(1)
        lCnt += 1
        if (lCnt % 10000 == 1):
            print "CNT:",lCnt