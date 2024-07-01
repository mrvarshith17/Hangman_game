import random
words = ['python', 'hangman', 'programming', 'computer', 'openai', 'artificial', 'intelligence']

def select_random_word(words):
    return random.choice(words)

def display_current_progress(word, guessed_letters):
    return ' '.join([letter if letter in guessed_letters else '_' for letter in word])

def play_hangman():
    word = select_random_word(words)
    guessed_letters = set()
    incorrect_guesses = 0
    max_incorrect_guesses = 6
    
    print("Welcome to Hangman!")
    
    while incorrect_guesses < max_incorrect_guesses:
        print("\nCurrent progress: " + display_current_progress(word, guessed_letters))
        print(f"Incorrect guesses left: {max_incorrect_guesses - incorrect_guesses}")
        guess = input("Guess a letter: ").lower()
        
        if guess in guessed_letters:
            print("You've already guessed that letter.")
            continue
        
        guessed_letters.add(guess)
        
        if guess in word:
            print(f"Good guess! '{guess}' is in the word.")
        else:
            incorrect_guesses += 1
            print(f"Sorry, '{guess}' is not in the word.")
        
        if all(letter in guessed_letters for letter in word):
            print("\nCongratulations! You've guessed the word: " + word)
            break
    else:
        print(f"\nYou've run out of guesses. The word was: {word}")

if __name__ == "__main__":
    play_hangman()