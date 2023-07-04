import random
import time

# Welcome message
print("\n----WELCOME TO HANGMAN GAME---- \n")

# Get the player's name
name = input("Enter your name: ")
print("Hello " + name + "  Good Luck!")

# Wait for 1 second
time.sleep(1)

# Start the game
print("Let's play Hangman!")
time.sleep(2)

def main():
    # Global variables
    global count
    global display
    global word
    global already_guessed
    global length
    global play_game

    # List of words to guess
    words_to_guess = [" delhi" , "mumbai" ,"bangalore" ,"kolkata" ,"chennai" ,"hyderabad" ,"ahmedabad" ,"pune" ,"jaipur" ,"lucknow" ,"chandigarh" ,"kochi" ,"indore" ,"bhopal" ,"patna" ,"kanpur" ,"nagpur" ,"agra" , "varanasi" ,"surat"  ,"vadodara" ,"ludhiana" ,"bhubaneswar" ,"indore" ,"amritsar" ,"ranchi"]
    
    # Select a random word from the list
    word = random.choice(words_to_guess)
    length = len(word)
    count = 0
    display = '_' * length
    already_guessed = []
    play_game = ""

def play_loop():
    # Global variable
    global play_game
    
    # Ask the player if they want to play again
    play_game = input("Do you want to play again? y = yes, n = no \n")
    
    # Validate the input
    while play_game not in ["y", "n","Y","N"]:
        play_game = input("Do You want to play again? y = yes, n = no \n")
    
    # Play again or exit the game
    if play_game == "y":
        main()
    elif play_game == "n":
        print("Thanks For Playing!")
        exit()

def hangman():
    # Global variables
    global count
    global display
    global word
    global already_guessed
    global play_game
    
    # Set the maximum number of wrong guesses
    limit = 5
    
    # Get the player's guess
    guess = input("This is the Hangman Word(!!it's a Major City!!): " + display + " Enter your guess: \n")
    guess = guess.strip()
    
    # Validate the guess
    if len(guess.strip()) == 0 or len(guess.strip()) >= 2 or guess <= "9":
        print("Invalid Input, Try a letter\n")
        hangman()
    elif guess in word:
        # Correct guess
        already_guessed.extend([guess])
        index = word.find(guess)
        word = word[:index] + "_" + word[index + 1:]
        display = display[:index] + guess + display[index + 1:]
        print(display + "\n")
    elif guess in already_guessed:
        # Already guessed letter
        print("Try another letter.\n")
    else:
        count += 1
        
        # Print the hangman based on the number of wrong guesses
        if count == 1:
            time.sleep(1)
            print("   _____ \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("Wrong guess. " + str(limit - count) + " guesses remaining\n")
        elif count == 2:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("Wrong guess. " + str(limit - count) + " guesses remaining\n")
        elif count == 3:
           time.sleep(1)
           print("   _____ \n"
                 "  |     | \n"
                 "  |     |\n"
                 "  |     | \n"
                 "  |      \n"
                 "  |      \n"
                 "  |      \n"
                 "__|__\n")
           print("Wrong guess. " + str(limit - count) + " guesses remaining\n")
        elif count == 4:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("Wrong guess. " + str(limit - count) + " last guess remaining\n")
        elif count == 5:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |    /|\ \n"
                  "  |    / \ \n"
                  "__|__\n")
            print("Wrong guess. You are hanged!!!\n")
            print("The word was:",already_guessed,word)
            play_loop()
    
    if word == '_' * length:
        print("Congrats! You have guessed the word correctly!")
        play_loop()
    elif count != limit:
        hangman()

# Start the game
main()
hangman()
