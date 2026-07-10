#creating class train , which has methods to book a ticket , get status of the train and get fare information 
class Train:
    def __init__(self , name , fare , seats):
        self.name = name
        self.fare = fare
        self.seats = seats

    def bookTicket(self):
        if self.seats > 0:
            print(f"Your ticket has been booked! Your seat number is {self.seats}")
            self.seats -= 1
        else:
            print("Sorry! No seats available")
    
    def getStatus(self):
        print(f"The name of the train is {self.name}")
        print(f"The seats available in the train are {self.seats}")

    def getFareInfo(self):
        print(f"The fare of the train is {self.fare}")

#creating an object of the class 
t1 = Train("Rajdhani Express" , 1500 , 5)
t1.getStatus()
t1.getFareInfo()
print()
t1.bookTicket()
t1.getStatus()

