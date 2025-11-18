import random

def get_secret_word ():

    word = input("Write the secret word").lower()
    
    while not word.isalpha:
        print("The secret word can only have letters")
        word = input("Write the secret word").lower()
    
    return word

def show_progress (secret_word, guessed_letters):
    guessed = ''
    for letter in secret_word:
        if letter in guessed_letters:
            guessed += letter
        else:
            guessed += "_"
    return guessed
    



def juego_ahorcado():

    secret_word =get_secret_word
    guessed_letters = []
    attempts = 5
    finished_game = False

    print("Welcome to game 'El Ahorcado'")
    print(f"You have {attempts} attempts to guess the secret word")
    print(show_progress(secret_word, guessed_letters), "The number of letters in the secret word is:",len(secret_word) )

    while not finished_game and attempts > 0:
        guessing = input(" Enter a letter").lower()
        if len(guessing) !=1 or not guessing.isalpha():
            print("Please type a valid letter")

        elif guessing in guessed_letters:
            print("You've already use that letter, try another one.")
        
        else:
            guessed_letters.append(guessing)

            if guessing in secret_word:
                print(f"You got it the letter {guessing} in the word ")
            
            else:
                attempts -= 1
                print(f"Sorry, {guessing} is not in the word secret")
                print(f"You have {attempts} attempts left")
        current_progress = show_progress(secret_word, guessed_letters)
        print(current_progress)

        if "_" not in current_progress:
            finished_game = True
            print(f"¡Congratulations, you won! the secret word is {secret_word}. ")
    if attempts==0:
        print(f"Sorry the attempts are over, the secret word was {secret_word}. ")


juego_ahorcado()








    




