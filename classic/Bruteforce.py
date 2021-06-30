from datetime import datetime

class Dictionary:
    def __init__(self, alphabet):
        self.matrix = alphabet
        self.total_length = len(alphabet)
        self.sub_len = []
        for i in range(self.total_length):
            self.sub_len.append(len(alphabet[i]))
        self.map = {}
        self.start()

    def start(self):
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i]) - 1):
                self.map[self.matrix[i][j]] = self.matrix[i][j + 1]
            if i != len(self.matrix) - 1:
                self.map[self.matrix[i][-1]] = self.matrix[i + 1][0]
            else:
                self.map[self.matrix[i][-1]] = self.matrix[0][0]

    def first_character(self, position):
        return self.matrix[position][0]

    def last_character(self, position):
        return self.matrix[position][-1]

    def next_character(self, character):
        return self.map[character]

    def length(self):
        return self.total_length


def char_range(first, last):
    char_list = []
    for char in range(ord(first), ord(last) + 1):
        char_list.append(chr(char))
    return char_list


lower_case = char_range("a", "z")
upper_case = char_range("A", "Z")
numbers = char_range("0", "9")

SHORT_DICTIONARY = Dictionary([lower_case])
NORMAL_DICTIONARY = Dictionary([lower_case, upper_case])
SECURE_DICTIONARY = Dictionary([lower_case, upper_case, numbers])
# SUPER_SECURE_DICTIONARY = Dictionary([lower_case, upper_case, numbers])

def next_string(string, dictionary):
    if len(string) == 0:
        return dictionary.first_character(0)
    final_char = string[-1]
    if final_char == dictionary.last_character(dictionary.length() - 1):
        return next_string(string[:-1], dictionary) + dictionary.first_character(0)
    else:
        return string[:-1] + dictionary.next_character(final_char)

def velocity_test():
    m = "aaaaaa"
    instante_inicial = datetime.now()
    while len(m) == 6:
        m = next_string(m,SHORT_DICTIONARY)
    instante_final = datetime.now()
    tiempo = instante_final - instante_inicial
    print(tiempo.seconds)