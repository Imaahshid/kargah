import random

words = ["apple", "python", "computer", "book", "school"]

word = random.choice(words)

guessed = ""
chances = 6

print("Welcome to Hangman!")

while chances > 0:

 for letter in word:
    if letter in guessed:
        print(letter, end=" ")
    else:
        print("_", end=" ")

print()

if all(letter in guessed for letter in word):
    print("You won!")
    break

guess = input("Guess a letter: ").lower()

if guess in guessed:
    print("You already guessed this letter!")
    continue

guessed += guess

if guess in word:
    print("Correct!")
elif
    chances -= 1
    print("Wrong!")
    print("Chances left:", chances)

elif
    print("You lost!")
    print("The word was:", word)