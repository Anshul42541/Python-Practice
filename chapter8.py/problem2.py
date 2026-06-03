#program for converting celsius to fahrenite using function
def celsius_to_fahrenhite(celsius):
    fahrenhite = (celsius *9/5) +32
    return fahrenhite

#taking input from user
celsius = float(input("Enter the temperature in celsius to convert into Fahrenheit: "))
print("The temperature in Fahrenheit is:", celsius_to_fahrenhite(celsius))