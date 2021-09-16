# find diffrence between odd position digit sum and even position
x=str(input('input your number'))
y=len(x)
even=0
odd=0
for i in range(0, y) :
    if (i%2==0):
        even+=int(x[i])
    else:
        odd+=int(x[i])
print("diffrence of odd and even= ", odd-even)

