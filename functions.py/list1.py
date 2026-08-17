#function to print the elements of the list in single line 
#normally if we print item one by one it prints each item in single line but we want all items in single line 

def print_elements(list):
    for item in list:
        print(item, end = " ") # here we modified the print function 

a = [2,6,58,6,9]

print_elements(a)