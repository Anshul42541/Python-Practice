list1 = ["anshul", "anmol" , "rohit" , "kabadi"]

name = input("Enter name to search in a list :")
if name in list1:
    print(f"{name} is present in the list")
else: 
    print(f"{name} is not present in the list")