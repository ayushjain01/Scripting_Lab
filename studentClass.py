class Student():
    def __init__(self,num):
        self.num = num
        self.accept()
    def display(self):
        print(f"Student Name - {self.name}\nStudent Age - {self.age}\nMarks - {self.marks}")
    def accept(self):
        self.name = input(f"Enter Student {self.num} Name : ")
        self.age = int(input(f"Enter Student {self.num} Age : "))
        self.marks = list(map(float, input(f"Enter Student {self.num} Marks : ").split(" ")))

object1 = Student(1)
object1.display()
object2 = Student(2)
object2.display()