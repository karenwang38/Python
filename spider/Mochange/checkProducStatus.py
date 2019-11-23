from MoChange import *
import time
import math


time_period = 5 #min

start_time = time.time()
while True:
    end_time = time.time()
    if (end_time - start_time) <= (time_period*60):
        InventoryWrite2File(False, 'status.text')
    else:
        print('### times up for status checking ###')
        break
