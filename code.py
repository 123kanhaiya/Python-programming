#0,0,2,1,4,2,6,3,8,4,10,5...

n= int(input())
a=0
b=0
for i in range(1,n+1):
    if (i%2==0):
        b+=1
    else:
        a+=2
if (n%2==0):
    print('{}'.format(b-1))
else:
    print('{}'.format(a-2))