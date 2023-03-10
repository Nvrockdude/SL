from functools import reduce
from collections import Counter
f=open("counting.txt")
#make a text file say counting.txt(in same folder)
contents=f.read().split()
print("\nFile Contents:")
print(*contents,sep=' ')
count_dict = Counter(contents)
print("\n\n",count_dict)
print("\n10 Words in decreasing order of occurance:")
s=(sorted(count_dict.items(),key=lambda x:x[1],reverse=True))
print(s[:10])
wordlen=[len(i) for i,j in s[:10]]
print("\nList with length of each word:\n",wordlen)
avg=(reduce(lambda x,y:x+y,wordlen))/len(wordlen)
print("Avg: ",avg)
sq_odd=[i*i for i in wordlen if i%2!=0]
print("Square of odd numbers: \n",sq_odd)
