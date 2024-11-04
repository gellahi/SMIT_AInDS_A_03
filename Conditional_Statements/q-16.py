side1=float(input("Enter the first side of the triangle: "))
side2=float(input("Enter the second side of the triangle: "))
side3=float(input("Enter the third side of the triangle: "))
if side1==side2==side3:
    print("The triangle is an equilateral triangle.")
elif side1==side2 or side2==side3 or side3==side1:
    print("The triangle is an isosceles triangle.")
else:
    print("The triangle is a scalene triangle.")