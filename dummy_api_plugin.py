from plugin import Plugin
import requests


class DummyApiPlugin(Plugin):
    def __init__(self, url, username, password):
        self.url = url
        self.username = username
        self.password = password
        self.token = None

    def connectivity(self):
        endpoint = f"{self.url}/auth/login"
        try:
            response = requests.post(endpoint, json={'username': self.username, 'password': self.password})
            if response.status_code == 200:
                data = response.json()
                self.token = data.get('token')
                print(data)
                return True
            else:
                print("Failed attempt in connecting:", response.status_code)
                return False
        except requests.RequestException as e:
            print(f"error: {e}")
            return False
