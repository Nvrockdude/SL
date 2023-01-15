class Reverse:
    string=""
    def __init__(self,string):
        self.string=" ".join(reversed(string.split()))
       

print("Enter 3 strings")
objArr=[]
countVowels = [0, 0, 0]
dict = {}
for i in range(3):
    objArr.append(Reverse(input()))
    for j in range(len(objArr[i].string)):
        #Counting the vowels
        if objArr[i].string[j].lower() in ['a', 'e', 'i', 'o', 'u']:
             countVowels[i] += 1
    
    dict.update({objArr[i].string:countVowels[i]})
print("Sorted in descending order of vowels in each")
print(*sorted(dict.items(),key=lambda x:x[1],reverse=True),sep="\n")
