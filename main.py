from RSA.RSA import RSA
from Vigenere.VigenereCipher import VigenereCipher
from Transposition.TranspositionCipher import TranspositionCipher

if __name__ == "__main__":
    rsa = RSA()
    vig_cipher = VigenereCipher('abcdefghijklmnop', 'spam')
    transposition_cipher = TranspositionCipher()
    rsa.generate_key_pair()
    print("Public Key:", rsa.public_key_pair)
    print("Private Key:", rsa.private_key_pair)
    print("Correct keypair:", str(rsa.check_key_pairs()))
    print("Encryption and Decryption working ? -> ", rsa.decrypt(rsa.encrypt("Hi There, how are you doing?")) == "Hi There, how are you doing?")
