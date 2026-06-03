#Building a game of stone paper scissors

#importing random module to generage randon numbers
import random

genrated_input = random.choice([1,2,3])

print("---LETSS PLAY STONE PAPER SCISSORS GAME!---")
consent = input("PRESS ENTER TO PLAY | ENTER \"0\" TO QUIT THE GAME")

while consent != "0":
    #taking input from the user 
    user_input = input("Enter What You Choose [stone , paper , scissors]: " )

    user_dict = {"stone":1,"paper":2,"scissors":3} 
    user = user_dict[user_input]  #assigning numerical value to the user input 

    reverse_dict= {1: "stone", 2:"paper",3:"scissors"}
    # we will use this dictionary to perform operations

    print(f"Computer Choose : {reverse_dict[genrated_input]} | You choose : {reverse_dict[user]}")
    if genrated_input == user:
        print("---Match Draw---")
    else:
        if genrated_input == 1 and user == 2:
            print("---YOU WIN!---")
        elif genrated_input== 1 and user == 3:
            print("---COMPUTER WIN!---")
        elif genrated_input==2 and user == 1:
            print("---COMPUTER WIN!---")
        elif genrated_input==2 and user == 3:
            print("---YOU WIN!---")
        elif genrated_input==3 and user == 1:
            print("---YOU WIN!---")
        elif genrated_input==3 and user == 2:
            print("---COMPUTER WIN!---")
        else:
            print("Try Again , Sorry !")


print("THANKS FOR PLAYING THE GAME !")

