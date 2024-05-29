from RSA.RSA import RSA

if __name__ == "__main__":
    rsa = RSA()
    rsa.generate_key_pair()
    print("Public Key:", rsa.public_key_pair)
    print("Private Key:", rsa.private_key_pair)
    print("Correct keypair:", str(rsa.check_key_pairs()))
    print("Encryption and Decryption working ? -> ", rsa.decrypt(rsa.encrypt("Hi There, how are you doing?")) == "Hi There, how are you doing?")

