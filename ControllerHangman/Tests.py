import unittest

from Controller.Controller import Controller, ControllerException
from RepositoryHangman.Repository import Repository


class Tests(unittest.TestCase):
    def setUp(self) -> None:
        self.__repository = Repository("test_file.txt")
        self.__controller = Controller(self.__repository)

    def test_add_sentence(self):
        self.__controller.add_sentence("Marra are mere")
        self.assertEqual(len(self.__repository.sentence_list), 6)
        print(self.__repository.sentence_list)
        with self.assertEqual(ControllerException):
            self.__controller.add_sentence("Mara are mere")
        with self.assertEqual(ControllerException):
            self.__controller.add_sentence("Eu si el mergem la mare")

