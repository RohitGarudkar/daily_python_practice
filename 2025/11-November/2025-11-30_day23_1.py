#Program to Calculate the Area and Circumference of a Circle
def circle(r):
    pi = 3.14  
    print("Area of a circle :",pi*r*r)
    print("Cricumerference of a circle :",round((2*pi*r),2))
    
num = int(input("Enter the redius of the circle to print the are and curcumference "))
circle(num)
