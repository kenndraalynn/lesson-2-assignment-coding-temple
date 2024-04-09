# Task 1: Identify the Greatest
"""
Write a Python program that prompts the user to enter three numbers. 
The program should then identify and print out the largest number among the three.
"""

x = int(input("Please enter a number: "))
y = int(input("Please enter a different number: "))
z = int(input("Please enter a another number: "))

if x > y and x > z:
    print("The largest number is ", x)
elif y > x and y > z:
    print("The largest number is ", y)
else:
    print("The largest number is ", z)


# Task 2: Identify the Smallest
"""
Extend your program from Task 1 to also determine the smallest number among the three and print it out.
"""

if x < y and x < z :
    print("The smallest number is ", x)
elif z == y or z == x and x < z and y:
    print("The smallest number is ", x)
elif y < x and y < z:
    print("The smallest number is ", y)
elif y == x or y == z and y < x and z:
    print("The smallest number is ", y)
elif z < x and z < y:
    print("The smallest number is ", z)
elif z == x or z == y and z < x and y:
    print("The smallest number is ", z)
else:
    print("There is no smallest number")


# Task 3: Equality Check
"""
Enhance your program to handle cases where two or all of the numbers are equal. 
The program should display appropriate messages like 
"Two numbers are equal and the largest" or "All numbers are equal".
"""

if x == y and z > x and y:
    print("There are two numbers equal to each other, and ", z, "is the largest number")
elif z == x and y > z and x:
    print("There are two numbers equal to each other, and ", y, "is the largest number")
elif y == z and x > z and y:
    print("There are two numbers equal to each other, and ", x, "is the largest number")
elif y == z and y > z and x:
    print("There are two numbers equal to each other, and ", y, "is the largest number")
elif x == y and x > z and y:
    print("There are two numbers equal to each other, and ", x, "is the largest number")
elif z == x and z > x and y:
    print("There are two numbers equal to each other, and ", z, "is the largest number")
elif y == z and z == x:
    print("All of the numbers are equal")
else:
    print("None of the numbers are equal")


