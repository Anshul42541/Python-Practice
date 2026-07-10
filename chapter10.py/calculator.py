#creating a class calculator which performs square and cube of a number

class calculator:
    def __init__(self , n):
        self.n = n
    def square(self):
        print(f"the square is {self.n*self.n}")
    def cube(self):
        print(f"the cube is {self.n*self.n*self.n}")

#creating object of class calculator 
a = calculator(5)
a.square()
a.cube()