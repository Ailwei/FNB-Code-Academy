# controll statemets

num = 0
if num > 0:
    print("this is positve number")
elif num == 0:
    print("this is zero")
else:
    print("the number is either zero or  nagative")
    
#input values

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

if (num1 > num2):
    print(num1 , "is greater than", num2)
elif num2> num1:
    print(num2, "is greater than", num1)
else:
    print("Both numbers are equal")
