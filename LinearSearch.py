numlist=[]
pos=0
element=int(input("enter how many numbers: "))
for i in range(1,element+1):
    value=int(input("enter the values: "))
    numlist.append(value)
print(numlist)
x=int(input("enter the number to search: "))
for j in range(len(numlist)):
    if(numlist[j]==x):
        print("element found")
        pos=j+1
        print("element found at: ",pos," in",numlist)
        break
else:
    print("not found")
