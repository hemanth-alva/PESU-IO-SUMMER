l1=[]
def mysearch(l1,low,high,key):
	pos=-1
	found=0
	while(low<=high and found==0):
		mid=int((low+high)/2)
		if(l1[mid]==key):
			pos=mid
			found=1
		elif (key<l1[mid]):
			high=mid-1
		else:
			low=mid+1
	return pos
m=input("enter the elements of the list").split(",")
key=int(input("enter the number to be searched\n"))
for x in m:
	l1.append(int(x))
l1.sort()
n=(len(l1)-1)
res = mysearch(l1,0,n,key)
if(res==-1):
	print("not found")
else:
	print("found at",res)

	
 
