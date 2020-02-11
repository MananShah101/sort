numlist=[]
x=int(input("enter how many numbers: "))
for k in range(1,x+1):
	v=int(input("enter values: "))
	numlist.append(v)
print(numlist)
for i in range(len(numlist)):
	minpos=i
	for j in range(i,len(numlist)):
		if(numlist[j]<numlist[minpos]):
			minpos=j
	temp=numlist[i]
	numlist[i]=numlist[minpos]
	numlist[minpos]=temp
print(numlist)
