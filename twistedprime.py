"""x=str(input("enter any prime number :- "))
x=x[::-1]
y=int(x)
print(y)"""

y=23
for i in range (2,y):
    if (y%i==0):
        break
    print('Not a Twisted Prime number')
        
    else:
    print('Twisted Prime number')


