import random

words = [
    "apple", "python", "computer", "book", "school", "planet", "garden",
    "window", "monkey", "castle", "orange", "purple", "summer", "winter",
    "rocket", "dragon", "camera", "flower", "guitar", "island", "jungle",
    "knight", "laptop", "magnet", "needle", "office", "pencil", "rabbit",
    "silver", "tiger", "umbrella", "violet", "wallet", "yellow", "zebra",
    "animal", "bottle", "candle", "dinner", "engine", "forest", "garden",
    "hammer", "insect", "jacket", "kitten", "ladder", "mirror", "nature"
]

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
    else:
        chances -= 1
        print("Wrong!")
        print("Chances left:", chances)

if chances == 0:
    print("You ran out of chances!")
    final_guess=input("Guess the whole word:").lower()
    if final_guess == word:
        print("you won!")
    else:
     print("You lost!")
     print("The word was:", word)
