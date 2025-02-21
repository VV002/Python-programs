# Purpose: To check if the given year is a leap year or not
def leap_year_checker(n):
    if n%4==0:
        if n%100!=0:
            return True
        elif n%400==0:
            return True
    else:
        return False

while(True):
    year = int(input("Enter the year: ")) #Input the year
    length=len(str(year)) #Calculating the length of the year
    if length<4 or length>4:
        print("Please enter a valid year, Try again!!")
    else:
        if leap_year_checker(year): #Function call to check if the year is a leap year
            print(f"{year} is a leap year")
        else:
            print(f"{year} is not a leap year")
        break
