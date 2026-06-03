num1 = int(input("Enter First Number : "))
num2 = int(input("Enter Second Number : "))
num3 = int(input("Enter Third Number : "))
num4 = int(input("Enter Fourth Number : "))

greatest = num1 
if num2 > greatest:
    greatest = num2
if num3 > greatest:
    greatest = num3
if num4 > greatest:
    greatest = num4    

print(f"{greatest} is greatest")
