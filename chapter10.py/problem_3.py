#creating a demo class , which has a class attribute 
class demo:
    def __init__(self):
        print("Class object created succesfully!")

    #initialzing class attribute 
    a = 10


#Now creating an object of class
number = demo()
print(number.a) #instance attribute not yet created so it will print class attribute value
#trying to change class variable through object 
number.a = 20  
print(number.a)  #instance attribute created so it will print instance attribute value

print(demo.a)  #this will still print class attribute value as instance attribute is created for object number and it will not affect class attribute value