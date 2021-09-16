n= [int(d)for d in str(input())]
even,odd=0,0
for i in range(0,len(n)):
	if i %2==0:
		even+=n[i]
	else:
		odd+=n[i]
k=(abs(odd+even))
print(k)
if k %3==0:
	print(k, 'divisible')
else:
	print(k,'not divisible')