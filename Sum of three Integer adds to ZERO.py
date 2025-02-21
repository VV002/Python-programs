#Function that finds the triplets whose sum is zero
def triplets_sum_zero(list):
    n=len(list)
    triplet_found=False #Flag to check if the triplets are found or not
    for i in range(n-2):
        for j in range(i+1,n-1):
            for k in range(j+1,n):
                if (list[i]+list[j]+list[k]==0):
                    print(f"The triplets whose sum is zero are: {list[i]} {list[j]} {list[k]}")
                    triplet_found=True
    #Incase no triplets exits
    if triplet_found==False:
        print("No triplets whose sum is zero exists")

#Getting the list of integers from the user using list comprehension
print("Enter the list of integers: ",end="")
list=[int(x) for x in input().split()]
print(f"The given list: {list}")

#Function call
triplets_sum_zero(list)
