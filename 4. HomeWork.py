import random
from array import array

#countOfQuestion=int(input("Hello. It`s game for you.\nEnter count of questions :: "))
countOfQuestion=random.randint(1,5)
i=0
res=0
mark=12/countOfQuestion
finalMark=0
mas=[0]*countOfQuestion
print(mark)
while i<countOfQuestion:
    firstNum = random.randint(1, 20)
    secondNum = random.randint(1, 20)
    mas.append(firstNum*secondNum)
    for item in mas:
        if firstNum*secondNum==item:
            firstNum = random.randint(1, 20)
            secondNum = random.randint(1, 20)
            resUser = int(input(f"{firstNum} * {secondNum} = "))
            if firstNum * secondNum == resUser:
                print("Good!!")
                finalMark += mark
            else:
                print("Bad. Try again.")
            i += 1
        elif firstNum*secondNum!=item:
            resUser = int(input(f"{firstNum} * {secondNum} = "))
            if firstNum * secondNum == resUser:
                print("Good!!")
                finalMark += mark
            else:
                print("Bad. Try again.")
            i += 1
print(f"Good. Your final mark :: {finalMark}")