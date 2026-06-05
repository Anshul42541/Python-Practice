#In this chapter , we will learn about file handling in python 

#TRYING TO READ A FILE 
f = open("d:\\Desktop\\python\\chapter9.py\\myfile.txt")
data = f.read()
print(data)
f.close()