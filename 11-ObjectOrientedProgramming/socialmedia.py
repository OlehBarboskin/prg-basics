class SocialMediaProfile:
    def __init__(self, username):
        self.username = username
        self.posts = []

    def add_post(self, content):
        self.posts.append(content)
        print(f"{self.username} added a new post: {content}")

    def display_timline(self):
        print(f"{self.username}")
        for post in self.posts:
            print (f'{post}')
JohnDoe = SocialMediaProfile("username")
JohnDoe.add_post ("Hello, world!")
JohnDoe.add_post ("Had a great day at the park!")
JohnDoe.add_post ("What's up, Natalie? How are you?")
JohnDoe.display_timline()