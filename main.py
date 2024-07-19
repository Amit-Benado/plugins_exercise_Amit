from dummy_api_plugin import DummyApiPlugin


def main():
    url = "https://dummyjson.com"
    username = "emilys"
    password = "emilyspass"
    plugin = DummyApiPlugin(url, username, password)

    plugin.run()

if __name__ == '__main__':
    main()
