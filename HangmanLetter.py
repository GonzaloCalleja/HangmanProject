
# Object of this class will contain a char and its intended behaviour in the game

alphabet = "abcdefghijklmnopqrstuvwxyz"


class HangmanLetter(object):

    def __init__(self, char):

        self.char = char
#        self.in_word = False
        self.discovered = False

    def __str__(self):
        if self.discovered:
            return self.char + " "
        else:
            return "_ "

    def __eq__(self, other):
        if other is self.char:
            return True
        else:
            return False


class HangmanWord(object):

    def __init__(self, word):

        self.letters = []
        for char in word:
            self.letters.append(HangmanLetter(char))

# override len()
    def __str__(self):
        result = ""
        for letter in self.letters:
            result += str(letter)

        return result

    def __contains__(self, item):
        if item in self.letters:
            return True
        else:
            return False

