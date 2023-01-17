"""Create a Python class called ‘Student’ having ‘name’, ‘age’ as attribute along with a list having the marks obtained for three subjects.
    - Create a constructor to initialize two objects of this class.
    - Create a member function called ‘display’ printing the details of a specific object
    - Ask user to enter the values for an object through an ‘accept’ member function.
    - Display these details.
"""

#Create Student Class
class Student():
    def __init__(self):
        self.name = ""
        self.age = 0
        self.marks = []
    #Display member function
    def display(self):
        print(f"Student Name - {self.name}\nStudent Age - {self.age}\nMarks - {self.marks}")
    #ask user to enter values through accept member function
    def accept(self):
        self.name = input(f"Enter Student Name : ")
        self.age = int(input(f"Enter Student Age : "))
        self.marks = list(map(float, input(f"Enter Student Marks : ").split(" ")))
#initialize two objects
object1 = Student()
object1.accept()
object1.display()
object2 = Student()
object2.accept()
object2.display()