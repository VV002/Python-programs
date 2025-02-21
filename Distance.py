import math
#Function to calculate distance from origin
def distance(x,y):
    return math.sqrt(x*x+y*y)

#without math module : return (x*x+y*y)**0.5

#taking input from user
x,y = int(input("Enter the x co-ordinate: ")),int(input("Enter the y co-ordinate: "))
print(f"Distance from ({x},{y}) to origin is {distance(x,y)}")



 