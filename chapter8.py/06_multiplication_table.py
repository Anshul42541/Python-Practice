#function for printing the Multiplication table of a given number
def multiplication_table():
    n = int(input("Enter a number to print its multiplication table: "))
    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")
    return f"Multiplication table of {n} is printed."

# Sample input
print(multiplication_table())
print(multiplication_table())

