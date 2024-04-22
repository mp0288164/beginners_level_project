def add(x,y):
    return x+y
def subtract(x,y):
    return x-y
def myltiply(x,y):
    return x*y
def divide(x,y):
    return x/y
print('select operation.')
print('1.Add')
print('2.subtract')
print('3.multiply')
print('4.divide')
choice=input('enter choice(1,2,3,4):-')

if choice in ('1','2','3','4'):
    try:
        number1=float(input("enter the first number:-"))
        number2=float(input('enter the second number:-'))
    except:
        print('Invaild input.please enter a number')
        #continue
    if choice=='1':
        print(number1,'+',number2,'=',add(number1,number2))
    elif choice=='2':
        print(number1,'-',number2,'=',subtract(number1,number2))
    elif choice=='3':
        print(number1,'*',number2,'=',multiply(number1,number2))
    elif choice=='4':
        print(number1,'/',number2,'=',divide(number1,number2))
else:
    print('Invalid Input')
