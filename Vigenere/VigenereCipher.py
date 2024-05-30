
class VigenereCipher:

    def __init__(self, alphabet: str, password: str):
        self.alphabet = alphabet
        self.password = [self.alphabet.index(char) for char in password]

    def _vigenere(self, message: str, encrypt: bool):
        step = encrypt * 2 - 1
        num_coded = [self.alphabet.index(char) if char in self.alphabet else char for char in message]
        result = [
            self.alphabet[(char + step * key) % len(self.alphabet)] if isinstance(char, int) else char
            for char, key in zip(num_coded, self.password * (int(len(message) / len(self.password)) + 1))
        ]
        return ''.join(result)

    def encode(self, message: str):
        return self._vigenere(message, True)

    def decode(self, message: str):
        return self._vigenere(message, False)
