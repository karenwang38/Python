'''

import tkinter as tk
root=tk.Tk()     #建立視窗容器物件


root.title('猜幾A幾B')  #視窗title
root.geometry('500x500')
       #將元件放入容器

e = tk.Entry(root,show=None)  #建立輸入方格
e.pack()   #將元件放入容器

def click():
    global info = e.get()
    label.config(text= info)

button=tk.Button(root, text='Enter', command=click)  #建立按鈕
button.pack()     #將元件放入容器

label=tk.Label(root, text='輸入') #建立標籤物件
label.pack()
root.mainloop()
'''

import tkinter as tk

window = tk.Tk()
window.title('my window')
window.geometry('300x300')
e = tk.Entry(window,show=None)
e.pack()

def insert_point():
    var = e.get()
    t.insert('insert',var)

def insert_end():
    var = e.get()
    t.insert('end',var)
b1 = tk.Button(window,text='insert point',width=15,
            height=2,command=insert_point)
b1.pack()
b2 = tk.Button(window,text='insert end',
               command=insert_end)
b2.pack()
t = tk.Text(window,height=2)
t.pack()

window.mainloop()
