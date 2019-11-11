import tkinter as tk
from tkinter import ttk
from MoChange import *



# (視窗title): 加入購物車
# ID:
# 商品編號：
# (商品編號輸入框)
# (按鈕)：加入購物車
# (按鈕):購物車清單
# (按鈕):清除購物車
# (按鈕):付款
computer = 'mac'

root=tk.Tk()     #建立視窗容器物件
root.title("購物車") # 視窗飄提名稱
root.geometry("560x380") # 視窗大小


context_label=tk.Label(root) # "ID"顯示
cartlist_label=tk.Label(root) # "購物車清單" 顯示
number_label = tk.Label(root, text="商品編號") # "商品編號"

number_entry=tk.Entry(root, text='number', width=20) # "商品編號" 輸入框

# 帳號選單（下拉式選單）
comboExample = ttk.Combobox(root,
                            values=[
                                    "llibs38",
                                    "karenwang38",
                                    "chctrader",
                                    "chctrader001",
                                    "big",
                                    "bigwife"])
print(dict(comboExample))
comboExample.grid(column=0, row=1)
comboExample.current(1)


def callbackFunc(event):
    select_id = ''
    print(comboExample.current(), comboExample.get())
    if comboExample.get() == 'llibs38':
        select_id = 'x59Ku3STtesGvZvOW47GwcXyL49sbZIKmmXVv29ChJU='
    elif comboExample.get() == 'karenwang38':
        select_id = 'VejRb/EsbgKN/qhEvWjYMCUYSJB6Mb4lloQtiXZUK2M='
    elif comboExample.get() == 'chctrader':
        select_id = 'fQwZvdt7kUOqM9iD8fkVdR6v1p+O3vmTeDu576xX+mI='
    elif comboExample.get() == 'chctrader001':
        select_id = '+Uu9D00ve1t3R7rP/aLxZTfLAItED5rJx7pOEY/SIrY='
    elif comboExample.get() == 'big':
        select_id = 'McHvxIefazHIGc8aJ+Qr/MO9kTIZ0c86tcT/EO5pdW0='
    elif comboExample.get() == 'bigwife':
        select_id = 'LEaQKEFNEYu162lrP3E7UAP2D2UpSdVJikadItCtfSw='

    context_label.configure(text="ID: " + select_id)
    print('context_label.get()', )
    return select_id


def AddCartButton():
    select_id = ''
    if comboExample.get() == 'llibs38':
        select_id = 'x59Ku3STtesGvZvOW47GwcXyL49sbZIKmmXVv29ChJU='
    elif comboExample.get() == 'karenwang38':
        select_id = 'VejRb/EsbgKN/qhEvWjYMCUYSJB6Mb4lloQtiXZUK2M='
    elif comboExample.get() == 'chctrader':
        select_id = 'fQwZvdt7kUOqM9iD8fkVdR6v1p+O3vmTeDu576xX+mI='
    elif comboExample.get() == 'chctrader001':
        select_id = '+Uu9D00ve1t3R7rP/aLxZTfLAItED5rJx7pOEY/SIrY='
    elif comboExample.get() == 'big':
        select_id = 'McHvxIefazHIGc8aJ+Qr/MO9kTIZ0c86tcT/EO5pdW0='
    elif comboExample.get() == 'bigwife':
        select_id = 'LEaQKEFNEYu162lrP3E7UAP2D2UpSdVJikadItCtfSw='
    else:
        select_id = 'No this Account'
    number = number_entry.get() or 'NUMBER'
    context_label.configure(text="ID: " + select_id + "\n NUMBER: " + str(number))
    AddCart(select_id,number)

def CartListButton():
    list = ''
    if comboExample.get() == 'llibs38':
        email = 'llibs38@gmail.com'
    elif comboExample.get() == 'karenwang38':
        email = 'karen.wang38@gmail.com'
    elif comboExample.get() == 'chctrader':
        email = 'chctrader@gmail.com'
    elif comboExample.get() == 'chctrader001':
        email = 'chctrader001@gmail.com'
    else:
        email = 'wrong email'

    if email != 'wrong email':
        List = CartList(email, computer)
        for cartList in List:
            list = list + cartList + '\n'

        print('list: ', list)
        cartlist_label.configure(text=list)
    else:
        cartlist_label.configure(text=email)

def CleanCartButton():
    select_id = ''
    if comboExample.get() == 'llibs38':
        select_id = 'x59Ku3STtesGvZvOW47GwcXyL49sbZIKmmXVv29ChJU='
    elif comboExample.get() == 'karenwang38':
        select_id = 'VejRb/EsbgKN/qhEvWjYMCUYSJB6Mb4lloQtiXZUK2M='
    elif comboExample.get() == 'chctrader':
        select_id = 'fQwZvdt7kUOqM9iD8fkVdR6v1p+O3vmTeDu576xX+mI='
    elif comboExample.get() == 'chctrader001':
        select_id = '+Uu9D00ve1t3R7rP/aLxZTfLAItED5rJx7pOEY/SIrY='
    elif comboExample.get() == 'big':
        select_id = 'McHvxIefazHIGc8aJ+Qr/MO9kTIZ0c86tcT/EO5pdW0='
    elif comboExample.get() == 'bigwife':
        select_id = 'LEaQKEFNEYu162lrP3E7UAP2D2UpSdVJikadItCtfSw='
    else:
        select_id = 'No this Account'

    ClearCart(select_id)

def PaymentButton():
    list = 'fail'
    select_id = ''
    if comboExample.get() == 'llibs38':
        select_id = 'x59Ku3STtesGvZvOW47GwcXyL49sbZIKmmXVv29ChJU='
        select_email = 'llibs38@gmail.com'
    elif comboExample.get() == 'karenwang38':
        select_id = 'VejRb/EsbgKN/qhEvWjYMCUYSJB6Mb4lloQtiXZUK2M='
        select_email = 'karen.wang38@gmail.com'
    elif comboExample.get() == 'chctrader':
        select_id = 'fQwZvdt7kUOqM9iD8fkVdR6v1p+O3vmTeDu576xX+mI='
        select_email = 'chctrader@gmail.com'
    elif comboExample.get() == 'chctrader001':
        select_id = '+Uu9D00ve1t3R7rP/aLxZTfLAItED5rJx7pOEY/SIrY='
        select_email = 'chctrader001@gmail.com'
    elif comboExample.get() == 'big':
        select_id = 'McHvxIefazHIGc8aJ+Qr/MO9kTIZ0c86tcT/EO5pdW0='
    elif comboExample.get() == 'bigwife':
        select_id = 'LEaQKEFNEYu162lrP3E7UAP2D2UpSdVJikadItCtfSw='
    else:
        select_id = 'No this Account'

    payResult = Payment(select_id,select_email,computer)
    cartlist_label.configure(text=payResult)





# count=0
# def clickOK():
#     global count
#     count=count + 1
#     label.configure(text="Click OK " + str(count) + " times")
#
# buttonOK=tk.Button(root, text="OK", command=clickOK)

# "加入購物車" 按鈕，執行加入購物車"AddCartButton"
button=tk.Button(root, text="加入購物車", command=AddCartButton)
button＿cartlist=tk.Button(root, text="清單", command=CartListButton)
button＿cartclean=tk.Button(root, text="清除購物車", command = CleanCartButton)
button＿payment=tk.Button(root, text="付款", command = PaymentButton)


# 選完帳號之後執行，帶入ID
comboExample.bind("<<ComboboxSelected>>", callbackFunc)

comboExample.pack()

context_label.pack()


number_label.pack()
number_entry.pack()

button.pack()
button_cartlist.pack()
button_cartclean.pack()
button_payment.pack()
cartlist_label.pack()



root.mainloop()
