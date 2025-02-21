def power_of_2(n):
    print(f"Table of the Power of 2 till {n}:") #Printing the power of 2 till n
    for i in range(n+1):
        print(f"2^{i} = {2**i}")

while(True):
    n = int(input("Enter the number(between 0 to 31): ")) #Input the number
    if n>=0 and n<=31:
        power_of_2(n)
        break
    else:
        print("Please enter a valid number, Try again!!")
        