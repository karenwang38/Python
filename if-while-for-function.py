# if else
user = int(input('Enter your salary:'))
if user < 50000:
    print('poor')
else:
    print('rich')

'''
Enter your salary:3829742
rich
'''

# for
print('----- for -----')
for i in range(8,19):
    print("i = ", i)

'''
i =  8
i =  9
i =  10
i =  11
i =  12
i =  13
i =  14
i =  15
i =  16
i =  17
i =  18
'''

print('----- while -----')
i = 5
while i<=10:
    print("i=", i)
    i=i+1

print('----- function: f() -----')
i = 10
def f():
    print(i)

i = 42
f()
# 42

print('----- function: addf(x,y) -----')
def addf(x,y):
    print(x+y)

i1=23
i2=12
addf(i1,i2)
# 35

print('----- function: return -----')

def myreturn(a, x=2, y= 3):
    return  a*x*y

i3=2
i4=5
i5=myreturn(8,i3,i4)
print(i5)
# 80

print("----- 迴圈結構for -----")
words=['airplane','cat','dog','bear','car']
print(words)
for w in words:
    print(w,len(w))

print("----- 使用者自訂函數 -----")
def ask_ok(prompt,retries=5,remider='Please try again'):
    while True:
        ok=input(prompt)
        if ok in ('yes'):
            return True
        if ok in ('no'):
            retries = retries-1
            print('tetries=',retries)
            if retries<0:
                raise ValueError('invalid user response')
            print(remider)
        if (not(ok in('no'))) & (not(ok in('yes'))):
            raise ValueError('invalid user response')


ask_ok("leave for yes or no: ")
'''
leave for yes or no: no
Please try again
leave for yes or no: no
Please try again
leave for yes or no: no
Please try again
leave for yes or no: yes
'''
