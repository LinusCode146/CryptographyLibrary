import math
import random

from Util import Util


class RSA:
    def __init__(self, bit_length=1024):
        self.bit_length = bit_length
        self.prime1: int = 0
        self.prime2: int = 0
        self.N: int = 0
        self.e: int = 0
        self.d: int = 0
        self.phi: int = 0
        self.__private_key_pair = None
        self.__public_key_pair = None

    def generate_primes(self):
        self.prime1 = Util.generate_large_prime(self.bit_length)
        self.prime2 = Util.generate_large_prime(self.bit_length)
        while self.prime1 == self.prime2:
            self.prime2 = Util.generate_large_prime(self.bit_length)

    def generate_module(self):
        self.N = self.prime1 * self.prime2

    def generate_encryption_exponent(self):
        self.phi = (self.prime1 - 1) * (self.prime2 - 1)
        possible = []
        if math.gcd(self.e, self.phi) != 1:
            for i in range(3, self.phi - 1):
                if math.gcd(i, self.phi) == 1:
                    if len(possible) > 7:
                        self.e = random.choice(possible)
                        break
                    possible.append(i)
        self.e = random.choice(possible)

    def generate_decryption_exponent(self):
        self.d = Util.mod_inverse(self.e, self.phi)

    def generate_key_pair(self):
        self.generate_primes()
        self.generate_module()
        self.generate_encryption_exponent()
        self.generate_decryption_exponent()
        self.public_key_pair = (self.e, self.N)
        self.private_key_pair = (self.d, self.N)

    def check_key_pairs(self):
        return (self.e * self.d) % self.phi == 1

    def encrypt(self, message):
        m = int.from_bytes(message.encode(), 'big')
        c = pow(m, self.e, self.N)
        return c

    def decrypt(self, message):
        m = pow(message, self.d, self.N)
        decoded = m.to_bytes((m.bit_length() + 7) // 8, 'big').decode()
        return decoded

    @property
    def public_key_pair(self):
        return self.__public_key_pair

    @property
    def private_key_pair(self):
        return self.__private_key_pair

    @public_key_pair.setter
    def public_key_pair(self, pair):
        self.__public_key_pair = pair

    @private_key_pair.setter
    def private_key_pair(self, pair):
        self.__private_key_pair = pair
