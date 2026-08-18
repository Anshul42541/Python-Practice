#we created a class Student which takes a name and marks of three subjects as parameters in the constructor 
# it also have a method to calculate and print average of the marks of student 

class Student:  #creating class 
    def __init__(self, name , marks1 , marks2 , marks3):  # creating parameterized constructor 
        self.name = name
        self.mark1 = marks1
        self.mark2 = marks2
        self.mark3 = marks3
        print("Student Created...")

    def Average(self):   # method to calc average and print 
        avg = (self.mark1 + self.mark2 + self.mark3) / 3 
        print(f"Average of marks of the student {self.name}  = {avg}")

s1 = Student("Anshul" , 80 ,50 , 90) #initializing the class object with its values 
s1.Average()  #calling method of the class through instance of the class 