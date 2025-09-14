import random
from hangman_art import stages
from hangman_wordlist import word_list
print("********************Welcome to Hanged man game********************************")
print("********************Guess the word in less than 6 attempts********************")
print("********************You can only guess one letter at a time*******************")
print("********************Good Luck*************************************************")
#Get random letter form list. 
chosen_word = random.choice(word_list).lower()
placeholder = len(chosen_word) * "_"

correct_list = []
print(placeholder)
game_over = False
stage_count = 6

while game_over == False:
    Display_value = ""
    user_input = input("Guess a letter: ")

    for letter in chosen_word:
        if letter == user_input:
            Display_value += letter
            correct_list.append(user_input)
        elif letter in correct_list:
            Display_value += letter
        else:
            Display_value += "_"
    if user_input not in chosen_word:
        stage_count -= 1
    if stage_count == 0:
        print("*********************you loose**************************************************")
        print("The correct word is " + chosen_word)
        game_over = True
    print("********************you have " + str(stage_count) + " lives left*************************************")
    print(stages[stage_count])    
    print(Display_value)

    if "_" not in Display_value:
        game_over = True
        print("********************you Won****************************************************")



