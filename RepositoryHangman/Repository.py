class Repository:
    def __init__(self, file_name):
        self.__file_name = file_name
        self.sentence_list = list()
        self.load_file()

    def load_file(self):
        file = open(self.__file_name, 'rt')
        for line in file.readlines():
            line = line.removesuffix("\n")
            self.sentence_list.append(line)
        file.close()

    def save_file(self):
        file = open(self.__file_name, 'wt')
        for sentence in self.sentence_list:
            sentence += "\n"
            file.write(sentence)
        file.close()

    def add_sentence(self, sentence_to_add):
        self.sentence_list.append(sentence_to_add)
        self.save_file()
