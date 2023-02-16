from RepositoryHangman import *


class ControllerException(Exception):
    pass


class Controller:
    def __init__(self, repository):
        self.__repository = repository

    def add_sentence(self, new_sentence):
        """
        the function checks if the new sentence has at least 1 word and if the new sentence is unique
        after that verifies each words length to be at least 3
        :param new_sentence: the sentence that needs to be add
        """
        new_sentence = new_sentence.strip()
        if not new_sentence:
            raise ControllerException("The sentence must contain at least 1 word!")
        if new_sentence in self.__repository.sentence_list:
            raise ControllerException("The sentence is already in the list of sentences!")
        list_of_characters = list(new_sentence)
        word_length = 0
        for i in range(len(list_of_characters)):
            if list_of_characters[i] != ' ':
                word_length += 1
            else:
                if word_length < 3:
                    raise ControllerException("Each word must have at least 3 letters!")
                word_length = 0
        self.__repository.add_sentence(new_sentence)