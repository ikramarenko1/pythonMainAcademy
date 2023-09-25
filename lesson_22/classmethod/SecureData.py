# Захист даних під час передачі через мережу:
# Створіть клас для представлення конфіденційних даних, які передаються через мережу.
# Використовуйте властивості для автоматичного шифрування та розшифрування даних перед передачею та при отриманні.
class SecureData:
    def __init__(self, data, key):
        self._key = key
        self._encrypted_data = self._encrypt(data, key)

    def _encrypt(self, data, key):
        return ''.join(chr(ord(char) ^ ord(key[i % len(key)])) for i, char in enumerate(data))

    def _decrypt(self, encrypted_data, key):
        return self._encrypt(encrypted_data, key)

    @property
    def data(self):
        return self._decrypt(self._encrypted_data, self._key)


secure_data = SecureData('Some Test Data', 'SecretKey')

print(secure_data.data)
