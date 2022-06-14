#  We are crerted a most basic game Rock paper scissors

# RULES OF GAME:
# Rock v/s Paper => paper
# Paper v/s  scissors => scissors
# Rock v/s Scissors => Rock

import random
options = ["Rock" , "Paper" , "Scissor"]
computer_option = random.choice(options)

def player_input():
    palyer_choice = input("Enter your choice player 1: ")
    return palyer_choice
    
def play_game(player_pick,computer_option):
    if(player_pick == 'Rock'):
        if(computer_option == 'Paper'):
            return -1
        elif(computer_option == 'Scissor'):
            return 1
        elif(computer_option == 'Rock'):
            return 0
        
    if(player_pick == 'Paper'):
        if(computer_option == 'Paper'):
            return 0
        elif(computer_option == 'Scissor'):
            return -1
        elif(computer_option == 'Rock'):
            return 1
            
    if(player_pick == 'Scissor'):
        if(computer_option == 'Paper'):
            return 1
        elif(computer_option == 'Scissor'):
            return 0
        elif(computer_option == 'Rock'):
            return -1
    
# First we take the player names
player_1 = input("Enter Your name Player 1 : ")
n = int(input("Enter how many rounds do you want to play: "))
print("****Welcome to Rock Paper Scissors Game*****")
print("choose form these option : \n[[Rock , Paper , Scissors]]")
print("Note: Choices are case Sensitive")

player_win_counter=0
computer_win_counter=0
tie_counter = 0

for i in range(n):
    player_pick = player_input()
    winner = play_game(player_pick,computer_option)
    print("Computer choice: "+computer_option)
    
    if(winner == 1):
        player_win_counter = player_win_counter + 1
        print(player_1+" Wins!")
        
    elif(winner == -1):
        computer_win_counter = computer_win_counter + 1
        print("Computer Wins!")
    elif(winner == 0):
        tie_counter = tie_counter + 1
        print("Its a tie")
        
if(player_win_counter > computer_win_counter):
    print("##### FINAL Winner is: "+player_1+" #####")
elif(computer_win_counter > player_win_counter):
    print("##### FINAL Winnner is Computer #####")
elif(computer_win_counter == player_win_counter):
    print("##### NO ONE WINS #####")
