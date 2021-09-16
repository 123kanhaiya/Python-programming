'''author : kanhaiya kumar gupta'''

firstnum=int(input('starting:-  '))
lastnum=int(input('ending :- '))
for num in range(firstnum,lastnum):
	if num>1:
		for i in range(2, num):
			if num%i==0:
				break
		else:
			print(num)
