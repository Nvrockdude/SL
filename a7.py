class Student:     
    def __init__(self):
        self.name=input("Enter student name:")
        self.age=input("Enter student age:")     
        self.marks=[]                                     

    def accept(self):#Accepting values through 'accept' function
        for i in range(3):
            self.marks.append(input("Enter subject "+str(i+1)+" marks"))

    def display(self): 
        print("Name: "+self.name)
        print("Age: "+self.age)
        print("Three subject marks are:")
        print(self.marks)

print("Student 1:")
s=Student()
s.accept()

print("Student 2:")
s1=Student()
s1.accept()
 
print("\nStudeunt 1");s.display()
print("\nStudeunt 2");s1.display()
