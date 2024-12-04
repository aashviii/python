# Practical Example 6: Write a Python program to check if a number is prime using if_else. 

n1 = int(input("Enter any number:"))
if n1>1:
    for i in range(2,n1):
        if n1 % i == 0:
            print(f"{n1} is not a prime number.")
            break 
    else:
        print(f"{n1} is a prime number")
else:
    print(f"{n1} is not a prime number.")