# Криптографія: Розробіть клас для шифрування та дешифрування тексту.
# Захистіть ключі та методи шифрування від доступу ззовні.
class Cryptography:
    def __init__(self, key):
        self.__key = key

    def __xor_cypher(self, text):
        return ''.join([chr(ord(char) ^ ord(self.__key[i % len(self.__key)])) for i, char in enumerate(text)])

    def encrypt(self, plaintext):
        return self.__xor_cypher(plaintext)

    def decrypt(self, cyphertext):
        return self.__xor_cypher(cyphertext)


new_key = Cryptography("secretkey")

encrypted_text = new_key.encrypt("bestpassword12345qwerty")
decrypted_text = new_key.decrypt(encrypted_text)

print(encrypted_text)
print(decrypted_text)
