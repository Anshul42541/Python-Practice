#creating a class programmer which takes name and language as input and displays the same

class Programmer:
    def __init__(self, name, language):
        self.name = name
        self.language = language
        print("programmer created")
    
    def display(self):
        print(f"Hello from {self.name} and  I am a programmer . Familiar with {self.language} language")

#creating am object of the class 
p1= Programmer("Anshul", "Python")

p1.display()