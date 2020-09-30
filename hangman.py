import random

words = [
    "baseball", 
    "basketball", 
    "soccer", 
    "football", 
    "tennis",
    "bowling",
    "lacrosse",
    "volleyball",
    "cheerleadering",
]

word_to_guess = words[random.randint(0, len(words))]
max_guesses = len(word_to_guess)/2

    

print("Let's play a game of hangman! ")
print("You have {} guesses to guess all the letter(s) in the word I am thinking of...".format((max_guesses)))

user_guess = input("Type a letter to start the game! What's your guess?   ")




