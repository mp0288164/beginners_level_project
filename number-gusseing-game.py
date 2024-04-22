import random
import math
low=int(input('enter the low number:-'))
high=int(input('enter the high number:-'))
x=random.randint(low,high)
print('you have only',round(math.log(high-low+1,2)),'chances to guess the integer.')
count=0
while count<math.log(high-low+1,2):
    count+=1
    guess=int(input('guess a numberL:-'))
    if x==guess:
        print("congratulations",count,"try!")
        break
    elif x>guess:
        print("number is to small")
    elif x<guess:
        print('number to high')

if count>=math.log(high-low+1,2):
    print('the number is:-',x)
    print('better luck next Time')