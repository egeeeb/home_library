class Book:
    def __init__(self, id, title, author, publisher, status, owner):
        self.id = id
        self.title = title
        self.author = author
        self.publisher = publisher
        self.status = status
        self.owner = owner

    def __str__(self):
        return f'id:{self.id}, title:{self.title}, author:{self.author}, status:{self.status}, owner:{self.owner}'