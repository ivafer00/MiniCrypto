class Vigenere():
    def __init__(self):
        self.plaintext = ""
        self.ciphertext = ""
        self.key = []

    def set_plaintext(self, message):
        self.plaintext = message

    def set_ciphertext(self, cipher):
        self.ciphertext = cipher

    def set_key(self, k):
        self.key = []
        for i in range(len(k)):
            self.key.append(int(k[i]))

    def cipher(self):
        self.ciphertext = ""
        for i in range(len(self.plaintext)):
            if self.plaintext[i].isalpha():
                code_ascii = 97
                if self.plaintext[i].isupper():
                    code_ascii = 65
                self.ciphertext += chr(((ord(self.plaintext[i]) % code_ascii + self.key[i % len(self.key)]) % 26) + code_ascii)
            else:
                self.ciphertext += self.plaintext[i]

    def decipher(self):
        self.plaintext = ""
        for i in range(len(self.ciphertext)):
            if self.ciphertext[i].isalpha():
                code_ascii = 97
                if self.ciphertext[i].isupper():
                    code_ascii = 65
                self.plaintext += chr(((ord(self.ciphertext[i]) % code_ascii - self.key[i % len(self.key)]) % 26) + code_ascii)
            else:
                self.plaintext += self.ciphertext[i]