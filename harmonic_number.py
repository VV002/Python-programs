def harmonic(n):#Function to calculate the harmonic number
    sum=1
    for i in range(2,n+1):
        sum+=1/i
    return sum

n = int(input("Enter the number: ")) #Input the number
print(f"The harmonic number of {n} is: {harmonic(n):.5f}") #Function call to calculate the harmonic number