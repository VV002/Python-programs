while(True):
    name=input("Enter your name: ")
    if len(name) < 3:
        print("Error: Name must be at least 3 characters, Try again!!")
    else:
        print(f"Hello {name}!!")
        break
