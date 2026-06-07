#write tables from 0 to 20 and save them in separate files

#creating a function for table 
def generate_table(n):
    table = ""                  #empty string to store the full table 
    for i in range(1, 11):
        table += f"{n} x {i} ={n*i}\n"
         #creating and opening in write mode
        with open(f"d:\\Desktop\\python\\chapter9.py\\tables\\table_of_{n}.txt", "w") as f: 
            f.write(table)      #writing the table in the file as already a string
    
    

#calling the function for tables from 2 to 20
for i in range(2, 21):
    generate_table(i)