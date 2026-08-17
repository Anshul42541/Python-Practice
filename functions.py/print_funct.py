#here we will discuss about the different properties of print function 
#like sep and end so sep and end are two attributes of print func. 
#by default sep value is space and end value is new line 

a = [ "anshul", "rohit", " 1" ]


for item in a : 
    print(item , end = " .... ", ) 
print()
# end defines what to be print or happen in the end of the line 

x = 25 
y = 65 
z = 100 

print(x,y,z , sep="_" , end=" ")
#sep defines how the different arguments will be separated