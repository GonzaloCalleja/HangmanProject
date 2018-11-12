from PIL import ImageTk, Image
from tkinter import *


alphabet = "abcdefghijklmnopqrstuvwxyz"

class HangmanGame:

    def __init__(self, word):

        print(word)

        word = word.lower()
        self.word = {}
        self.finished = False
        self.attempts = ""
        display = "_"

        for i in range(len(word)):
            self.word[i] = [word[i], display]

    def check(self, char):

        if char < "a" or char > "z" or len(char) != 1:
            raise Exception("Not valid Input")

        result = False
        for i in range(len(self.word)):
            if char in self.word[i]:
                self.word[i][1] = char
                result = True

        return result

    def get_hidden_word_array(self):
        result = []
        for i in self.word:
            result.append(self.word[i][1])
        return result

    def get_hidden_word(self):
        result = ""
        for i in self.word:
            result += self.word[i][1] + " "
        return result

    def play_in_console(self):

        penalty = 0

        while penalty < 10:
            hang = self.get_hidden_word()
            print(self.attempts)
            print(hang)
            print(penalty)
            attempt = input("Guess: ")
            if attempt in self.attempts or attempt in hang:
                print("You already tried that one!")
                continue
            try:
                if not self.check(attempt):
                    self.attempts += attempt
                    penalty += 1
            except Exception as error:
                print(error)

            if "_" not in self.get_hidden_word():
                break

        if penalty == 10:
            print("Lost")
        else:
            print("Win")

    # def print_canvas(self, canvas):
    #     size = 10, 10
    #     for i in range(5):
    #         letter_name = "name" + ".jpg"
    #         im = Image.open("JPEG/" + letter_name)
    #         im.thumbnail(size)
    #         canvas[i].image = ImageTk.PhotoImage(im)
    #         canvas[i].create_image(20, 60, image=canvas[i].image, anchor='nw')


class DrawHangman(object):

    def __init__(self):

        window = Tk(screenName="Hangman")
        bgcolor = "#AED6F1"
        window.title("Poker")
        window.geometry("900x400")

        self.frame = Frame(master=window, bg=bgcolor)
        self.frame.pack_propagate(0)  # Don't allow the widgets inside to determine the frame's width / height
        self.frame.pack(fill=BOTH, expand=1)  # Expand the frame to fill the root window

        self.label = Label(self.frame, text="Hangman Game", bg=bgcolor, fg="white")
        self.label.grid(row=0, column=0)
        self.label.config(font=("Courier", 15))

        # create a fram to display the game
        self.game = Frame(master=self.frame)
        self.game.grid(row=1, padx=20)

        self.errors = Frame(master=self.game)
        self.errors.grid(row=2, column=1)
        self.hangman = Frame(master=self.game)
        self.hangman.grid(row=2, column=2)
        self.choices = Frame(master=self.game)
        self.choices.grid(row=2, column=3)

        self.error_label = Label(self.errors, text="", bg="grey")
        self.error_label.pack()

        self.buttons = []

        row = 1
        for i in range(len(alphabet)):
            self.buttons.append(Button(master=self.choices, text=alphabet[i], command=lambda i=i: self.select(i)))
            self.buttons[i].grid(row=1, column=i)

        # self.bt2 = Button(self.frame, text="Exit Game", command=self.exit_game, bg="black", fg="yellow")
        # self.bt2.grid(row=1, column=1)

        window.mainloop()

    def exit_game(self):
        exit(0)

    def select(self, id):
        self.error_label["text"] += alphabet[id]


game = DrawHangman()
