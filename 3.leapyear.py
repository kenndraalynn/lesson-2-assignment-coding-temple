#Task 1: Leap Year Checker

user_year = int(input("Please enter a year: "))



if user_year % 4 == 0  and user_year % 100 != 0:
        print("That is a leap year!")
elif user_year % 400 == 0: 
    print("That is a leap year!")
else:
    print("That is not a leap year, try again.")





