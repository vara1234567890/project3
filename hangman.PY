import random

# List of words for the game
word_list = ['python', 'java', 'hangman', 'programming', 'developer']

def choose_word():
    """Randomly choose a word from the word list"""
    return random.choice(word_list)

def display_word(word, guessed_letters):
    """Display the current state of the word with guessed letters"""
    return ' '.join([letter if letter in guessed_letters else '_' for letter in word])

def hangman():
    word = choose_word()
    guessed_letters = []
    attempts = 6
    print("Welcome to Hangman!")

    while attempts > 0:
        # Display the current state of the word
        print(f"Word: {display_word(word, guessed_letters)}")
        print(f"Attempts left: {attempts}")
        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print("You already guessed that letter.")
        elif guess in word:
            guessed_letters.append(guess)
            print(f"Good guess! '{guess}' is in the word.")
        else:
            attempts -= 1
            print(f"Wrong guess! '{guess}' is not in the word.")

        # Check if the word is fully guessed
        if all(letter in guessed_letters for letter in word):
            print(f"Congratulations! You guessed the word: {word}")
            break
    else:
        print(f"Game Over! The word was: {word}")

if __name__ == "__main__":
    hangman()