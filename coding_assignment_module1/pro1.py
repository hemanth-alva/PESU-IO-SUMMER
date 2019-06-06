list=[] #to create a empty list
i=input("enter the numbers seperated by comma").split(",") #take the input
for m in i:
	list.append(int(m)) #to add the inputs into the list
print(list) 
print(tuple(list))
