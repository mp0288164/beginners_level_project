#first 
str=input('enter the string:-')
len=len(str)
L1=str[::-1]
print(L1)

#second
def res(x):
    return x[::-1]
mystr="my name is manisha prajapati ,i am leave in manasa"
rev=res(mystr)
print(mystr)
print(rev)

#third
def rev(x):
    str=''
    for i in  x :
        str=i+str
        print(str)
    return str
s='manisha'
print('The original string is:-',s)
print('reverse string is:-',rev(s))
s1=list(s)
s1.reverse()
str=''
for i in s1:
    str=str+i
print(str)

