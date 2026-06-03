#program for prime number 
num = int(input("Enter a number : "))

if num > 1:
    for i in range(2, num+1):
        if (num%2 == 0):
            print(f"{num} is not a prime number")
        elif (num%i == 0):
            print(f"{num} is prime number ")
        
print("End of program")