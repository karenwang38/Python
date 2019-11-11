# -*- coding: utf-8 -*-
#!/usr/bin/python

import os
import subprocess

res = subprocess.Popen('ps -ef | grep MainBeta',stdout=subprocess.PIPE,shell=True)
attn=res.stdout.readlines()
counts=len(attn)  #获取ASRS下的进程个数
print (counts)
if counts<10:    #当进程不够正常运行的个数时，说明某只程式退出了
    print('restart autoRun.py')
    os.system('python3 /Users/karenwang/Desktop/Program/Python/Exchange/TOKOK/MainBeta.py')     ##启动程式
##    os.system('reboot')    #重启系统
