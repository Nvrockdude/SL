# Write Python code to do the following:
# i. Create list with inputs from user
# ii. Determine minimum and maximum elements in the list
# iii. Insert new element into the list
# iv. Delete an element from the list
# v. Determine if an element is present in the list

li=[]
n= input("Enter number of elements")
print("Enter "+ n + " values")
for i in range(int(n)):
    li.append(int(input()))
li.insert(int(input("Enter pos")),int(input("Enter ele")))
print(li)
li.remove(int(input("Enter ele to del")))
print(li)
pos=li.index(int(input("Find ele")))
print("Element found at" + str(pos))
print(li)
print("MAX:"+str(max(li))+"\nMIN:"+str(min(li)))
print(li)
