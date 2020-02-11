numlist=[]
x=int(input("enter how many numbers: "))
for i in range(1,x+1):
    value=int(input("enter the values: "))
    numlist.append(value)
    numlist.sort()
print(numlist)
search=int(input("enter the number to search: "))
start=0
pos=0
end=len(numlist)-1
while(start<=end):
    mid=(start+end)//2
    if(search==numlist[mid]):
        print("element found")
        pos=mid+1
        print(pos)
        break
    elif(search<numlist[mid]):
        end=mid-1
    elif(search>numlist[mid]):
        start=mid+1
else:
    print("not found")
