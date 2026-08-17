#we will practice function working here 
#Function is used to perform a specific task n number of times in the program . it helps to reduce redundancy 

def hello_world():  #function declaration with or without parameters 
    print("HELLO WORLD...")

hello_world() #this is function calling statement with argument if needed 
hello_world()
hello_world()
hello_world()

#we can return a value in function to use that in future 
#i am writing a function to add two numbers and retrun their sum 
def Sum_of_two(a, b):
    sum= a + b
    print(sum)
    return sum 

print(Sum_of_two(1, 2)) #this will return 3 and if i did not return the sum it would give none value 

#we can also give default parameters to the function but Non-default argument follows default argument
#can set default value for all the parameterss also 
def prod_of_two(a, b=1):
    product = a*b
    print(f"{a} * {b} = {product}")

prod_of_two(2) #passing only one argument that is a
prod_of_two(2,2) #passing both argument 
#prod_of_two()  #no arguments will give error 
