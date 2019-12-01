from MoChange import *
from multiprocessing import Pool
from multiprocessing import Process
import multiprocessing as mp
import time

print('process number:', mp.cpu_count())


def AccountPay(mail):

    # initial parameter
    if mail == 'chctrader001@gmail.com':
        id = '+Uu9D00ve1t3R7rP/aLxZTfLAItED5rJx7pOEY/SIrY='
        computer = 'windows'
    elif mail == 'llibs38@gmail.com': # not use to pay
        id = 'x59Ku3STtesGvZvOW47GwcXyL49sbZIKmmXVv29ChJU='
        computer = 'asus'
    elif mail == 'karen.wang38@gmail.com':
        id = 'VejRb/EsbgKN/qhEvWjYMCUYSJB6Mb4lloQtiXZUK2M='
        computer = 'debbieS'
    elif mail == 'chctrader@gmail.com':
        id = 'fQwZvdt7kUOqM9iD8fkVdR6v1p+O3vmTeDu576xX+mI='
        computer = 'mac'
    elif mail == 'diabloiiiblizzard@gmail.com':
        id = 'Knnjqe9jKT8z0Kp1XzNoT3wSmoqDggIhtnNuFLUalMs='
        computer = 'pigpig'

    time_period = 4 #min

    # Login(mail, computer)
    # Payment('fQwZvdt7kUOqM9iD8fkVdR6v1p+O3vmTeDu576xX+mI=', 0, computer)
    start_time = time.time()
    while True:
            end_time = time.time()
            if (end_time - start_time) <= (time_period*60):
                print('執行時間：', end_time - start_time)
                print("email: ", mail, "\nid: ", id, '\n computer: ', computer)
                cart_list = CartList(mail, computer)
                print('loop car list', cart_list, ' mail: ', mail)
                # 購物車有東西後開始付款
                if cart_list != []:
                    print('購物車有東西: ', len(cart_list), mail , '\n',time.asctime( time.localtime(time.time()) ))
                    if Payment(id, 0, computer) == '庫存不足':
                        ClearCart(id)
                        print('庫存不足。清空購物車！')
                    else:
                        print('交易成功 or 交易錯誤')
                    print('付款時間: ', mail , '\n',time.asctime( time.localtime(time.time()) ))
                else:
                    print('購物車為空！')
                print(time.asctime( time.localtime(time.time()) ))
                print('#################################')
            else:
                print('購買時間截止！')
                break


if __name__ == '__main__':
    p = Pool(8) # 建立有5個程序的程序池
    mailList = ['chctrader@gmail.com',
                'chctrader001@gmail.com',
                'karen.wang38@gmail.com',
                'diabloiiiblizzard@gmail.com',
                'llibs38@gmail.com',
                'chctrader001@gmail.com',
                'chctrader@gmail.com',
                'diabloiiiblizzard@gmail.com',
                'karen.wang38@gmail.com',
                'llibs38@gmail.com',
                'chctrader@gmail.com',
                'diabloiiiblizzard@gmail.com',
                'karen.wang38@gmail.com',
                'llibs38@gmail.com',]
    # mailList = ['chctrader001@gmail.com', 'llibs38@gmail.com']
    # mailList = ['llibs38@gmail.com', 'chctrader@gmail.com']
    # print(p.map(f, [2,4,6])) # 將f函式的操作給程序池
    print(p.map(AccountPay, mailList))

# def f(name,age):
#     print ('hello', name, age)
#
# if __name__ == '__main__':
#     p = Process(target=f, args=('bob',2)) # p程序執行f函式，引數為'bob'，注意後面的“,”
#     p.start() # 程序開始
#     p.join() # 阻塞主執行緒，直至p程序執行結束
