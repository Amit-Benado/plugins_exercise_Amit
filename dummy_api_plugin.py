from plugin import Plugin


class DummyApiPlugin(Plugin):
    def __init__(self, url, username, password):
        self.username = username
        self.password = password
        self.url = url



