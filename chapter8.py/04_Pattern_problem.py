#function for printing a pattern of n lines

def  print_pattern(n):
    for i in range(n):
        print("*" * (n-i))

# Sample input
print_pattern(4)

'''    Output:
        ****
        ***
        **
        *
'''
