'''author : kanhaiya'''

n= [int(d)for d in str(input())]
even,odd=0,0
for i in range(0,len(n)):
	if i %2==0:
		even+=n[i]
	else:
		odd+=n[i]
k=(abs(odd-even))

if k %11==0:
	print( 'it is divisible')
else:
	print('it is not divisible')