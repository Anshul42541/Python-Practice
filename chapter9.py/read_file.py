#reading from a file 

f = open("d:\\Desktop\\python\\chapter9.py\\myfile.txt")
if f.readable():
    print(f.read())
f.close()