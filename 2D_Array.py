def arr(m,n):
    #Declaring an empty list to store the elements of the array
    array=[] 

    #Getting the elements of the array from the user
    for i in range(m):
        row = [] #Declaring a list to store the elements of the row
        for j in range(n):
            print(f"Enter the element for {i+1}th row and {j+1}th column: ",end="")
            a=int(input())
            row.append(a)
        array.append(row)
    return array

#Function to print the 2D array
def print_array(array,m,n):
        print("The 2D array is: ")
        for i in range(m):
            for j in range(n):
                print(array[i][j],end=" ")
            print("")


#Getting the no of rows and columns from the user
m = int(input("Enter the no of rows: "))
n = int(input("Enter the no of columns: "))
res=arr(m,n)
print_array(res,m,n)