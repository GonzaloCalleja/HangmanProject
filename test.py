import random
from HangmanDictionary import HangmanGame

words = open("words.txt", "r").read().split("\n")
while True:
    s = HangmanGame(random.choice(words))
    s.play_in_console()

    if input("Would you like to play again? (T / F)") is "F":
        break
