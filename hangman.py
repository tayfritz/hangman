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
max_guesses = round(max_guesses)

print("Let's play a game of hangman! ")
print("You have {} guesses to guess all the letter(s) in the word I am thinking of...".format((max_guesses)))
user_status = []

while max_guesses != 0:
    user_guess = input("Type a letter to play or type 'quit' to quit the game   ")

    if user_guess == "quit":
        break
    elif user_guess in word_to_guess:
        user_status.append(user_guess)
    else:
        print("Sorry, {} is not in the word I am thinking of.".format(user_guess))
        max_guesses -= 1
        print("You now have {} guesses left.".format(max_guesses))

if max_guesses == 0:
    print("Sorry, you ran out of guesses. The word I was thinking about was {}".format(word_to_guess))
    print("Here were your guesses.")
    print(user_status)

