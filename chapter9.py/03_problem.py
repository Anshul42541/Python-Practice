#WE will open a file and check if there is word "donkey"
#if the word is present we will replace it with hastags  and write to the file 

with open("d:\\Desktop\\python\\chapter9.py\\donkey.txt") as f:
    data = f.read()
    if "donkey" in data:
        with open("d:\\Desktop\\python\\chapter9.py\\donkey.txt", "w") as f:
            data = data.replace("donkey", "######")
            f.write(data)
            print("The word donkey is replaced with ###### in the file !")
    else:
        print("The word donkey is not present in the file !")
   