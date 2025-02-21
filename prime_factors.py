def check_prime(n):#Function to check if the number is prime or not
    if n>1:
        for i in range(2,n):
            if n%i==0:
                return False
        else:
            return True
    else:
        return False
n=int(input("Enter a number: ")) #Input the number
prime = [num for num in range(2,n+1) if check_prime(num)] #List to store the prime numbers
print(f"Prime Factors for {n} are: ",end=" ")
i=0
while(True):
    if n in prime:
        print(n,end=" ")
        break
    elif n%prime[i]==0:
        print(prime[i],end=" ")
        n=n//prime[i]
    else:
        i+=1
