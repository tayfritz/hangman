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
print(max_guesses)


for letters in word_to_guess:
    print(letters)


print("Let's play a game of hangman! ")
user_guess = input("Type a letter to start the gane! What's your first guess?   ")
