#we will create an static method inside a class 

class India:
    def __init__(self):
        pass

    @staticmethod #decorator 
    def Continent():   #no need of self parameter in static methods
        print("India lies in Asia Continent ")

    @staticmethod
    def sum(a,b,c):
        return a+b+c


India.Continent() #calling the static method using class name 
print(India.sum(5,6,9))