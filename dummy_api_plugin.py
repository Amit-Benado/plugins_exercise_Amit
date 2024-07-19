from plugin import Plugin
import requests


class DummyApiPlugin(Plugin):
    def __init__(self, url, username, password):
        self.url = url
        self.username = username
        self.password = password
        self.token = None

    def connectivity_test(self):
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

    def authenticated_user(self):
        # check if authentication was done
        if not self.token:
            return None

        # provided the token get current authenticated user
        address = f"{self.url}/user/me"

        try:
            # GET request with the Bearer token
            response = requests.get(address, {"Authorization": f"Bearer {self.token}"})
            if response.status_code == 200:
                data = response.json()
                return data
            else:
                print("Failed attempt:", response.status_code)
                return None
        except requests.RequestException as e:
            print(f"Error: {e}")
            return None

    def posts(self):
        # limit of 60 posts
        endpoint = f"{self.url}/posts?limit=60"
        try:
            #GET request
            response = requests.get(endpoint)
            if response.status_code == 200:
                data = response.json().get('posts')
                return data
            else:
                print("Failed attempt:", response.status_code)
                return None
        except requests.RequestException as e:
            print(f"Error retrieving posts: {e}")
            return None

    def comments(self):
        # posts with comments
        posts = self.posts()
        # array for comments per post
        comments_by_post = {}
        # go over posts
        for this_post in posts:
            endpoint = f"{self.url}/posts/{this_post['id']}/comments"
            try:
                response = requests.get(endpoint)
                if response.status_code == 200:
                    comment = response.json().get('comments')
                    comments_by_post[this_post] = comment
                else:
                    print(f"Failed attempt: {response.status_code}")
            except requests.RequestException as e:
                print(f"Failed attempt: {e}")
        return comments_by_post


