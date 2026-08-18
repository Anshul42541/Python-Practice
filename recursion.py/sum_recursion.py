#here we will calculate sum of first n natural numers using recursion 
def sum_of_natural_num(n):
    if n == 0: # base case 
        return 0

    sum = sum_of_natural_num(n-1) + n  #recursive case 
    return sum   # return statement 

print(sum_of_natural_num(5))