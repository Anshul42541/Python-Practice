#opening a file with "with" statement 

with open("d:\\Desktop\\python\\chapter9.py\\myfile.txt") as f:
    print(f.read())

#with the help of with statements we don't need to worry about closinf the file "with" statemnt close it automaticaly
