numlist=[]
x=int(input("enter how many elements: "))
for i in range(1,x+1):
	v=int(input("enter the value: "))
	numlist.append(v)
print(numlist)
for j in range(len(numlist)-1,0,-1):
	for h in range(j):
		if(numlist[h]>numlist[h+1]):
			temp=numlist[h]
			numlist[h]=numlist[h+1]
			numlist[h+1]=temp
print(numlist)
