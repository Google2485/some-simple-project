#Default function to implement condition to check leap year
def checkleap(year):
#checking if the year is leap year
    if (year % 4 == 0 and year % 100 != 0) or (year %400 == 0):
        print("Given year is a leap year")
#Else it is not a leap year
    else:
        print("Given year is not a leap year")
#Taking input from user
Year =int(input("Enter the number to cheak leap year or not: "))
#printing the result
checkleap(Year)