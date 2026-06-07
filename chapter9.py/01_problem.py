#reading a poem from a file and finding if it contains a specific word or not 

#opening the file in read mode
with open("d:\\Desktop\\python\\chapter9.py\\poem.txt") as f:
    #reading the file 
    data = f.read()

    #checking if the word "Twinkle" is present in the file or not
    if "tWinkle".lower() in data.lower():               # using lower() to ignore the case of the word 
        print("The word is present in the file")
    else:
        print("The word is not present in the file")