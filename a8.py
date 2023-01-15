from functools import reduce

urlist=[]
print("Enter 6 Numbers:\n")
for i in range(6):
    urlist.append(int(input()));
print(urlist)
ur2list=[(lambda x: 3*x) (x) for x in urlist]
print(ur2list)
print(reduce(lambda a,b:a+b,urlist))
