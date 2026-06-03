#finding double spaces in a string  and replacng them with single space 
abc = "this   is   a string "
print(abc.find("  "))

a = abc.replace("  ","")

print(a)