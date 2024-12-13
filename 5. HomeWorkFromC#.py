import os
import random
import time
from os import system

countOfQuestion = random.randint(1,5)

arr =[]
def init_array(input):
    i = 0
    while (i <= countOfQuestion):
        input.append(0)
        i += 1
def clear_console():
    if os.name == 'nt':  # Для Windows
        os.system('cls')
    else:  # Для Linux/macOS
        os.system('clear')
init_array(arr) #параметр передається по силці у функцію
#c = countOfQuestion
firstNum=0
secondNum=0
mark = 12.0/countOfQuestion
finalMark = 0.0
resUser = 0
i=0
while(i<countOfQuestion):
    i+=1
    firstNum = random.randint(1, 20)
    secondNum = random.randint(1, 20)
    for item in arr:
        if item ==(firstNum*secondNum):
            firstNum = random.randint(1, 20)
            secondNum = random.randint(1, 20)
            print(f"Mark by question :: {round(mark, 2)}")
            resUser = input(f"{firstNum} * {secondNum} = ")
            if int(resUser) == (firstNum * secondNum):
                print("Good!!")
                finalMark += mark
                arr[i] = firstNum * secondNum
                continue
            else:
                print("Bad!!. Try again!")

    clear_console()
    print(f"Mark by question :: {round(mark, 2)}")
    resUser = input(f"{firstNum} * {secondNum} = ")
    if int(resUser) == (firstNum * secondNum):
        print("Good!!")
        finalMark+=mark
        arr[i]=firstNum*secondNum
    else:
        print("Bad!!. Try again!")
    time.sleep(0.4)

clear_console()
print(f"Good. Your mark {finalMark}")