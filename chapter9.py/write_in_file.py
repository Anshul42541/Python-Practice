#writing in a file 

#opening a file in a write mode 
f = open("d:\\Desktop\\python\\chapter9.py\\myfile.txt","w")
#writing in the file 
if f.write("This is my first line in the file\n"):
    print("Data has been written in the file successfully")
f.close()