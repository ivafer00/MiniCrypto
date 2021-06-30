from classic.Statistics import *
class Caesar:
    def __init__(self):
        self.message = ""
        self.ciphertext = ""
        self.key = 0

    def cipher(self):
        self.ciphertext = ""
        for i in range(len(self.message)):
            if self.message[i].isalpha():
                init_ascii = 97
                if self.message[i].isupper():
                    init_ascii = 65
                self.ciphertext += chr(((ord(self.message[i]) % init_ascii + self.key) % 26) + init_ascii)
            else:
                self.ciphertext += self.message[i]

    def decipher(self):
        self.message = ""
        for i in range(len(self.ciphertext)):
            if self.ciphertext[i].isalpha():
                code_ascii = 97
                if self.ciphertext[i].isupper():
                    code_ascii = 65
                self.message += chr(((ord(self.ciphertext[i]) % code_ascii - self.key) % 26) + code_ascii)
            else:
                self.message += self.ciphertext[i]

    def set_cipher(self, c):
        self.ciphertext = c

    def set_message(self, m):
        self.message = m

    def set_key(self, k):
        key = str(k)
        if key.isdecimal():
            self.key = int(key)
        else:
            self.key = ord(k)

    def print(self):
        print("Plaintext: ", self.message)
        print("Ciphertext: ", self.ciphertext)
        print("Key: ", self.key)

    def bruteforce(self):
        print("Starting bruteforce...")
        for i in range(26):
            self.set_key(i)
            self.decipher()
            print("Valor", i, ":\t", self.message)
        print("Process has finished")

    def most_probably_result(self):
        valor = []
        for i in range(26):
            self.set_key(i)
            self.decipher()
            valor.append((i, xi(self.message).__getattribute__("statistic")))
        valor.sort(key=lambda x: x[1])
        print(valor)
        self.set_key(valor[0][0])
        self.decipher()
        return self.message