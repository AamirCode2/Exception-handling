try:
    age = int(input("Enter your age: "))
    
    if age*0!=0:
        raise ValueError
    if age%2==0:
        print("Your age is an even number.")
    else:
        print("Your age is an odd number.")
except ValueError:
    print("Your input has a ValueError, retry.")