#Function to calculate WindChill
def windchill_calculator(t,v):
    w = 35.74 + 0.6215*t + (0.4275*t - 35.75) * v**0.16
    return w


#taking input from user
while(True):
    temperature = float(input("Enter the temperature in Fahrenheit: "))
    wind_speed = float(input("Enter the wind speed in miles per hour: "))
    if temperature > 50 or wind_speed > 120 or wind_speed < 3:
        print("Enter valid input, Temperature should be less than 50 and wind speed should be between 3 and 120")
        print("Try again!!")
    else:
        result=windchill_calculator(temperature,wind_speed) #Function call to calculate WindChill
        print(f"Windchill is {result}")
        break