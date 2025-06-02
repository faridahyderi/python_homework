# hangman-closure.py

# Task 4: Closure Practice

def make_hangman(secret_word):
    guesses = []

    def hangman_closure(letter):
        guesses.append(letter.lower())
        display = ''.join([char if char in guesses else '_' for char in secret_word])
        print(display)

        return all(char in guesses for char in secret_word)

    return hangman_closure


# --- Main game logic ---

if __name__ == "__main__":
    secret = input("Enter the secret word: ").lower()  # secret word input
    hangman = make_hangman(secret)  # closure instance

    print("\nLet's play Hangman!\n")

    while True:
        guess = input("Guess a letter: ").lower()
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        is_complete = hangman(guess)
        if is_complete:
            print(f"Congratulations! You guessed the word: {secret}")
            break
