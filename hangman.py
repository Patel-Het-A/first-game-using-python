WORD_LIST = [
    "algorithm", "function", "variable", "compile", "iterate",
    "recursion", "binary", "array", "syntax", "pointer"
]

def display_header(attempts):
    print("HANGMAN")
    pointer = "^".rjust(attempts + 1)
    print(pointer)

def select_word():
    return random.choice(WORD_LIST)

def play_game():
    word = select_word()
    guessed_letters = set()
    correct_guesses = ["_"] * len(word)
    attempts = 0

    print("Welcome to Hangman!")

    while attempts < len("HANGMAN"):
        display_header(attempts)
        print(" ".join(correct_guesses))
        guess = input("Guess a letter: ").lower()

        # Input validation
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single alphabetical character.")
            continue

        # Check if letter is already guessed
        if guess in guessed_letters:
            print("You already guessed that letter. Try another one.")
            continue

        # Add guess to guessed letters set
        guessed_letters.add(guess)

        # Check if guess is in the word
        if guess in word:
            print("Good guess!")
            for idx, letter in enumerate(word):
                if letter == guess:
                    correct_guesses[idx] = guess
        else:
            print("Wrong guess!")
            attempts += 1

        # Check for win condition
        if "_" not in correct_guesses:
            print(f"Congratulations! You guessed the word: '{word}'")
            print("Phew... you are saved.")
            return

    # If out of attempts, print losing message
    print(f"You are hanged. The word was '{word}'.")



def main():
    while True:
        play_game()
        replay = input("Do you want to play again? (y/n): ").lower()
        if replay != 'y':
            print("Thanks for playing Hangman!")
            break

if __name__ == "__main__":
    main()
