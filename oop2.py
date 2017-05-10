class Student:
    simester=""
    counter=0
    def __init__(self,Name,Age):
        self.name=Name
        self.age=Age
        Student.counter +=1
    def get_data(self):
        return self.name, self.age
    def print_data(self):
        print("Name:",self.name)
        print("Age:",self.age)

#Use
std1=Student("Mohammed",28)
std2=Student("Ali",20)
print(std1.get_data()[0])
std1.simester="Hi"
#std1.grad=50
print(std1.simester)
std1.print_data()
print(getattr(std1,"name"))
print(hasattr(std1,"name"))
setattr(std1,"age",20)
print(std1.age,std1.counter)
print(Student.__name__)

