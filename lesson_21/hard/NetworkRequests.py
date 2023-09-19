# Мережеві запити: Реалізуйте клас для відправлення мережевих запитів (наприклад, HTTP запитів)
# та обробки відповідей. Захистіть дані, що відправляються та отримуються через мережу.
import requests
import base64


class NetworkRequest:
    def __init__(self, base_url):
        self.__base_url = base_url

    def __encode_data(self, data):
        encoded_data = base64.b64encode(data.encode()).decode()
        return encoded_data

    def __decode_data(self, data):
        decoded_data = base64.b64decode(data.encode()).decode()
        return decoded_data

    def send_request(self, endpoint, data):
        encoded_data = self.__encode_data(data)
        response = requests.post(f'{self.__base_url}/{endpoint}', data=encoded_data)
        decoded_response = self.__decode_data(response.text)
        
        return decoded_response
