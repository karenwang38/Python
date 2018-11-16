import sys
import random

'''
random_range =[3,4,5,6,7,9]
print(random_range)
print(random_range.index(6))
random_range.pop(3)
print(random_range)
'''

author = 'karen'
version = 'v0.1'


print("Guess", author +"'s heart!", "version:", version)
# Answer
random_range =[0,1,2,3,4,5,6,7,8,9]
num1=random.choice(random_range)
random_range.pop(random_range.index(num1))
num2=random.choice(random_range)
random_range.pop(random_range.index(num2))
num3=random.choice(random_range)
random_range.pop(random_range.index(num3))
num4=random.choice(random_range)

answer = [num1,num2,num3,num4]
print(answer)

'''
temp = [1,3,5,4]
guess = '1345'
print(str(temp[0]) == guess[0])
'''
start = True
while True:
    try:
        if (start):
            user_number = str(input("Enter 4 difference number: "))
            start = False

        #user_number_str = str(user_number)
        # check 4 number
        if len(user_number) != 4:
            raise ValueError("it needs \"4\" difference number")

        # check each number is differencd
        for i in range(0,3):
            for j in range(i+1,4):
                if(user_number[i]==user_number[j]):
                    raise ValueError("it needs 4 \"difference\" number")


        # ?A ?B
        A_cnt=0
        B_cnt = 0
        for ii in range(0,4):
            for jj in range(0,4):
                # A
                if((str(answer[ii]) == user_number[jj]) & (ii == jj)):
                    A_cnt = A_cnt+1
                elif(str(answer[ii]) == user_number[jj]):
                    B_cnt = B_cnt+1
        print(A_cnt, "A", B_cnt, "B")

        if(A_cnt != 4):
            print("try again")
            raise ValueError("it needs 4 \"difference\" number")
        print("Correct!!!!")

        break
    except ValueError:
        user_number = str(input("Please Enter 4 difference number:"))
    except:
        print("Unexpected error!!!", user_number)
        user_number = str(input("Please Enter 4 difference number:"))
