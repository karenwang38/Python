from MoChange import *
import time



# Login('karen.wang38@gmail.com')
# Payment('fQwZvdt7kUOqM9iD8fkVdR6v1p+O3vmTeDu576xX+mI=','chctrader@gmail.com')
# Payment('VejRb/EsbgKN/qhEvWjYMCUYSJB6Mb4lloQtiXZUK2M=','karen.wang38@gmail.com')
# Payment('x59Ku3STtesGvZvOW47GwcXyL49sbZIKmmXVv29ChJU=','llibs38@gmail.com')
# Payment('+Uu9D00ve1t3R7rP/aLxZTfLAItED5rJx7pOEY/SIrY=','chctrader001@gmail.com')
mail = 'chctrader001@gmail.com'
computer = 'mac'

if mail == 'chctrader001@gmail.com':
    id = '+Uu9D00ve1t3R7rP/aLxZTfLAItED5rJx7pOEY/SIrY='
elif mail == 'llibs38@gmail.com':
    id = 'x59Ku3STtesGvZvOW47GwcXyL49sbZIKmmXVv29ChJU='
elif mail == 'karen.wang38@gmail.com':
    id = 'VejRb/EsbgKN/qhEvWjYMCUYSJB6Mb4lloQtiXZUK2M='
elif mail == 'chctrader@gmail.com':
    id = 'fQwZvdt7kUOqM9iD8fkVdR6v1p+O3vmTeDu576xX+mI='

# Login(mail, computer)
# Payment('fQwZvdt7kUOqM9iD8fkVdR6v1p+O3vmTeDu576xX+mI=', 0, computer)
while True:
    print("email: ", mail, "\nid: ", id)
    # Payment(id, mail, computer)
    print('car list: ' ,CartList(mail), 'mail: ', mail)
    print('car list: ' ,CartList('karen.wang38@gmail.com'), 'mail: karen.wang38@gmail.com')
    print(time.asctime( time.localtime(time.time()) ))
