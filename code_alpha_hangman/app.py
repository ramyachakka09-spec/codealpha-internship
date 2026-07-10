import random

# List of predefined words
words = ["python", "coding", "computer", "program", "developer"]

# Randomly choose a word
word = random.choice(words)

# Store guessed letters
guessed_letters = []

# Maximum incorrect guesses
max_attempts = 6
wrong_attempts = 0

print("=" * 40)
print("        HANGMAN GAME")
print("=" * 40)
print("Guess the word one letter at a time.")
print(f"You have {max_attempts} incorrect guesses.\n")

while wrong_attempts < max_attempts:

    # Display the current progress
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "

    print("\nWord:", display)

    # Check if the word is fully guessed
    if "_" not in display:
        print("\n🎉 Congratulations! You guessed the word:", word)
        break

    # Get user input
    guess = input("Enter a letter: ").lower()

    # Validate input
    if len(guess) != 1 or not guess.isalpha():
        print("❌ Please enter only one alphabet letter.")
        continue

    # Check if already guessed
    if guess in guessed_letters:
        print("⚠ You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    # Check guess
    if guess in word:
        print("✅ Correct Guess!")
    else:
        wrong_attempts += 1
        print("❌ Wrong Guess!")
        print(f"Remaining Attempts: {max_attempts - wrong_attempts}")

# If user loses
if wrong_attempts == max_attempts:
    print("\n💀 Game Over!")
    print("The correct word was:", word)