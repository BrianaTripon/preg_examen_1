import random

from ControllerHangman.Controller import Controller, ControllerException
from RepositoryHangman.Repository import Repository


class UI:
    def __init__(self):
        self.repository = Repository("sentences")
        self.controller = Controller(self.repository)

    def start(self):
        while True:
            self.print_menu()
            option = input("Enter option: ").strip()
            if option == '1':
                new_sentence = input("Enter a new sentence you'd like to add: ")
                try:
                    self.controller.add_sentence(new_sentence)
                except ControllerException as e:
                    print(str(e))
            elif option == '2':
                self.hangman_game()
            elif option == '0':
                return
            else:
                print("Option does not exist!")

    def hangman_game(self):
        sentence_to_guess = random.choice(self.repository.sentence_list)
        letter_list_sentence_to_guess = list(sentence_to_guess)
        letters_to_print = []
        letters_to_print.append(letter_list_sentence_to_guess[0].lower())
        letters_to_print.append(" ")
        letters_to_print.append(letter_list_sentence_to_guess[-1].lower())
        for i in range(len(letter_list_sentence_to_guess)):
            if letter_list_sentence_to_guess[i] == " ":
                letters_to_print.append(letter_list_sentence_to_guess[i-1].lower())
                letters_to_print.append(letter_list_sentence_to_guess[i+1].lower())
        hangman_word = "hangman"
        hangman_letters = list(hangman_word)
        hangman_index = -1
        hangman_string = ""
        print(self.create_string_to_print(letter_list_sentence_to_guess, letters_to_print) + " - " + hangman_string)
        while True:
            letter_guessed = input("Enter guess: ")
            letter_guessed = letter_guessed.strip().lower()
            if (letter_guessed in letter_list_sentence_to_guess or letter_guessed.upper() in letter_list_sentence_to_guess) and letter_guessed not in letters_to_print:
                letters_to_print += letter_guessed
                print(self.create_string_to_print(letter_list_sentence_to_guess, letters_to_print) + " - " + hangman_string)
                if self.create_string_to_print(letter_list_sentence_to_guess, letters_to_print) == sentence_to_guess:
                    print("You Won! :)")
                    return
            else:
                hangman_index += 1
                hangman_string += hangman_letters[hangman_index]
                print(self.create_string_to_print(letter_list_sentence_to_guess, letters_to_print) + " - " + hangman_string)
                if hangman_string == hangman_word:
                    print("You Lost! :(")
                    return

    @staticmethod
    def create_string_to_print(letter_list_sentence_to_guess, letters_to_print):
        string_to_print = ""
        for i in range(len(letter_list_sentence_to_guess)):
            if letter_list_sentence_to_guess[i].lower() in letters_to_print:
                string_to_print += letter_list_sentence_to_guess[i]
            else:
                string_to_print += " _ "
        return string_to_print

    @staticmethod
    def print_menu():
        print("1. Add a new sentence")
        print("2. Play game")
        print("0. Exit")


ui = UI()
ui.start()
