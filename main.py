from dummy_api_plugin import DummyApiPlugin


def main():
    url = "https://dummyjson.com"
    username = "emilys"
    password = "emilyspass"
    plugin = DummyApiPlugin(url, username, password)

    success = plugin.connectivity_test()

    if success:
        print("Success.")
    else:
        print("Failed attempt.")


if __name__ == '__main__':
    main()
