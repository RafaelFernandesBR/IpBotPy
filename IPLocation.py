import requests


class IPLocation:
    def __init__(self):
        self.base_url = "http://ip-api.com/json/"

    def fetch(self, ip_address):
        params = {"lang": "pt"}
        url = self.base_url + ip_address
        response = requests.get(url, params=params)
        if response.status_code != 200:
            raise Exception("Falha ao buscar localização para o endereço IP")
        return response.json()
