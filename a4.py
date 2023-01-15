history=[]
def ktoc(a):
    return a-273.15
def ctok(a):
    return a+273.15
def ctof(a):
    return  1.8 * a + 32
def ftoc(a):
    return (a - 32)  / 1.8 
def ftok(a):
    return 273.5 + ftoc(a)
def ktof(a):
    return 1.8*(ktoc(a)) + 32
while(1):
    print("Main Menu".center(40,"#"))
    ch=int(input("1.Conversion\n2.History\n3.EXIT\nEnter your choice(int only):"))
    if ch==1:
        n=input("Enter temperature with unit(Eg:20C,50.00k...):")
        val=float(n[:-1])
        unit=n[-1].upper()
        to=input("Enter the unit to which u wanna convert(c/f/k)").upper()
        if unit=="K" and to=="C":
            ans=ktoc(val)
        elif unit=="K" and to=="F":
            ans=ktof(val)
        elif unit=="C" and to=="F":
            ans=ctof(val)
        elif unit=="C" and to=="K":
            ans=ctok(val)
        elif unit=="F" and to=="C":
            ans=ftoc(val)
        elif unit=="F" and to=="K":
            ans=ftok(val)
        else:
            print("Invalid input!!!")
            continue
        print("Ans:"+str(ans)+str(to))
        x=[val,unit,"to",round(ans,3),to]
        history.append(tuple(x))
    elif ch==2:
            print(history,sep="\n")
    elif ch==3:
        break
    else:
        print("Whats wrong with you!!!")
