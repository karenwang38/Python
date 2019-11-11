from MoChange import *
import time

# id_list = ['VejRb/EsbgKN/qhEvWjYMCUYSJB6Mb4lloQtiXZUK2M=', 'x59Ku3STtesGvZvOW47GwcXyL49sbZIKmmXVv29ChJU=', 'fQwZvdt7kUOqM9iD8fkVdR6v1p+O3vmTeDu576xX+mI=', '+Uu9D00ve1t3R7rP/aLxZTfLAItED5rJx7pOEY/SIrY=']
id_list = ['VejRb/EsbgKN/qhEvWjYMCUYSJB6Mb4lloQtiXZUK2M=']
start_time = time.time()
time_period = 10 # min
# 1 min = 60 sec = 60*60 micro sec

while True:
    end_time = time.time()
    print('start_time: ', start_time)
    print('end_time: ', end_time)
    print('start - end: ', end_time - start_time)
    print('============================')
    if (end_time - start_time) <= (time_period*60):
        print('購買票券...')
        for id in id_list:
            print(type(id))
            print("ID: ", id)
            Payment(id)
    else:
        print('停止購買。')
        break
    #time.sleep(0.2)
