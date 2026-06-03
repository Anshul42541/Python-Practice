#facorial of a given number using for loop 
num = int(input("Enter a number : "))
factorial = 1 

while num> 0:
    factorial *= num 
    num -= 1
print(f"{factorial} is the factorial of the given number")
