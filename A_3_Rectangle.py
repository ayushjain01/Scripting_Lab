"""Write a python program to create a class ‘Rectangle’. This class should include a constructor to initialize the dimensions. 
Include a function in the class to compute the area of the rectangle. Create objects of the class and print area."""

class rectangle():
    #Class should include a constructor
    def __init__(self,length, breadth):
        self.length = length
        self.breadth = breadth
    #Include function to calculate area
    def areaCal(self):
        return self.length*self.breadth
        
#Create Objects    
a = float(input("Enter Length of Rectangle 1 :"))
b = float(input("Enter Breadth of Rectangle 1 :"))
c = float(input("Enter Length of Rectangle 2 :"))
d = float(input("Enter Breadth of Rectangle 2 :"))
rect1 = rectangle(a,b)
rect2 = rectangle(c,d)
area1 = rect1.areaCal()
area2 = rect2.areaCal()
print(f"Area of rectangle 1 : {area1}")
print(f"Area of rectangle 2 : {area2}")
