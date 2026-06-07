# we will create a game function which returns a score and write it into a file, and then create another function which writes the high score in the file 
import random
def game():
    score = random.randint(0,100)

    #fetching the score from the file 
    with open("d:\\Desktop\\python\\chapter9.py\\Hi-Score.txt","r") as f:
        high_score = f.read()
        if high_score != "":                   
            high_score = int(high_score)        #converting the high score from string to integer bcoz read function returns a string
        else:
            high_score = 0                       #initialising the high score to 0 if the file is empty 
    
    print(f"your score: {score} and Hi-Score : {high_score}")
    #compare the score with high score and if the score is greater than updating it in the file 
    if score > high_score:
        with open("d:\\Desktop\\python\\chapter9.py\\Hi-Score.txt", "w") as f:
            score = str(score)
            f.write(score)
            print("your high score is updated !")

    return score

game()

    




