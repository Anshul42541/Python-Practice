#function to finf the factorial of n 
#solving these problem using recursion 

def find_factorial(n):
    if n == 1:
        return 1  # declaring the base case 
    fact = n * find_factorial(n-1) # recursive step to move closer to answer 
    return fact 

print(find_factorial(5))
print(find_factorial(10))
print(find_factorial(8))
