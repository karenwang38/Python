from MoChange import *
import time
import math

id = 'VejRb/EsbgKN/qhEvWjYMCUYSJB6Mb4lloQtiXZUK2M='
email = 'karen.wang38@gmail.com'
computer = 'mac'
itmeList = ['200044', '747', '750', '759', '624', '626', '628', '527', '509', '531', '593', '597', '683', '200200']
# itmeList = ['509']
time_flag = True

time_period = 4 # min
# 1 min = 60 sec = 60*60 micro sec

run_time = 1570420680 # 20191006 11:58
sleeptime = 1 # min
onlyAdd = True

if onlyAdd == False:
    Login(email)

if time_flag:
    # 檢查是否要開始
    while time_flag:
        now = time.time()
        print('### Not Start Runing ###')
        #開始後有時間限制！
        start_time = time.time()
        while now - run_time > 0:
            end_time = time.time()
            print('start_time: ', start_time)
            print('end_time: ', end_time)
            print('start - end: ', end_time - start_time)
            print('check time: ', time.asctime( time.localtime(end_time) ))
            print('=============time count===============', end_time - start_time)
            print('===================')
            print('===================')
            print('===================')
            if (end_time - start_time) <= (time_period*60):
                print('購買票券...')
                BuyTicket(id, 0, itmeList, False, onlyAdd, computer)
            else:
                print('停止購買。')
                time_flag = False
                break
            #time.sleep(3)
        if time_flag == False:
            break
        time.sleep(sleeptime*60)
else:
    BuyTicket(id, email, itmeList, True, onlyAdd, computer)
