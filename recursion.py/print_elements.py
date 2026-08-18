#function to print all elements of list using recursion 

def print_element(list , index):
    if index == len(list):
        return 
    print(list[index])
    print_element(list , index +1)

a = [1,2,3,8,6 , "Anshul "]
print_element(a , 0)
print_element(a , 2)