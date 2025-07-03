import claculate
length = float(input("Enter the lenth of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))

area = claculate.area(length, width)
perimeter = claculate.perimeter(length, width)

print(f"The area of the rectangle is {area}")
print(f"The area of the perimeter is {perimeter}")