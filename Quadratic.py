#Function to find the roots of the Quadratic Equation
def quadratic_equattion_roots(a,b,c):
    delta = b**2 - 4*a*c
    if delta > 0:
        print("Roots are real and different")
        root_1 = (-b + delta**0.5)/(2*a)
        root_2 = (-b - delta**0.5)/(2*a)
        print(f"Root 1: {root_1}\nRoot 2: {root_2}")
    elif delta == 0:
        print("Roots are real and same")
        root = -b/(2*a)
        print(f"Roots are : {root}")
    else:
        print("Roots are imaginary or Complex")
        print(f"Root 1: {(-b / 2*a)} + i {abs(delta**0.5) / 2*a}\nRoot 2: {(-b / 2*a)} - i {abs(delta**0.5) / 2*a}")


#taking input from user
a,b,c = int(input("Enter the value of a: ")),int(input("Enter the value of b: ")),int(input("Enter the value of c: "))
quadratic_equattion_roots(a,b,c)
