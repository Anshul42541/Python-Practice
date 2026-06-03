#function to Convert inches to centimeters 

def inches_to_cms():
    inches = float(input("Enter the length in inches: "))
    centimetres = inches * 2.54
    return f"{inches} inches is equal to {centimetres} centimeters."

# Example usage
print(inches_to_cms())