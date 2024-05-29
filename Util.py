import random


class Util:

    @staticmethod
    def is_probable_prime(n, k=128):
        if n in (2, 3):
            return True
        if n % 2 == 0 or n == 1:
            return False

        r, d = 0, n - 1
        while d % 2 == 0:
            r += 1
            d //= 2

        for _ in range(k):
            a = random.randint(2, n - 2)
            x = pow(a, d, n)
            if x == 1 or x == n - 1:
                continue

            for _ in range(r - 1):
                x = pow(x, 2, n)
                if x == n - 1:
                    break
            else:
                return False
        return True

    @staticmethod
    def generate_large_prime(bit_length):
        while True:
            candidate = random.getrandbits(bit_length)
            candidate |= (1 << (bit_length - 1)) | 1
            if Util.is_probable_prime(candidate):
                return candidate

    @staticmethod
    def extended_gcd(a, b):

        old_r, r = a, b
        old_s, s = 1, 0
        old_t, t = 0, 1

        while r != 0:
            quotient = old_r // r
            old_r, r = r, old_r - quotient * r
            old_s, s = s, old_s - quotient * s
            old_t, t = t, old_t - quotient * t

        return old_r, old_s, old_t

    @staticmethod
    def mod_inverse(e, phi):
        gcd, x, y = Util.extended_gcd(e, phi)
        if gcd != 1:
            raise ValueError("The multiplicative inverse doesn't exist!")
        else:
            return x % phi
