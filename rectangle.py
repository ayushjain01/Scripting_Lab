class rectangle():
    def __init__(length, breadth):
        self.length = length
        self.breadth = breadth
    def areaCal():
        self.area = self.lenght*self.breadth
    
a = float(input("Enter Length of Rectangle :"))
b = float(input("Enter Breadth of Rectangle :"))
rect = rectangle(a,b)
area = rect.areaCal()
print(f"Area of ractangle : {area}")