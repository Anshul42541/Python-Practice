#recursive function to calculate the sum of the first n natural numbers 

# Defining the function 

def sum_natural_numbers(num):
    # Base case: if num is 1 , return 1 
    if num == 1:
        return 1
    # Recursive case:
    else:
        return num + sum_natural_numbers(num-1)
    
#Sample input 
print(sum_natural_numbers(5)) 
print(sum_natural_numbers(10)) 
print(sum_natural_numbers(15)) 
print(sum_natural_numbers(20)) 
