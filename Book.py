
class Book:
    couter = 1

    def __init__(self, name, author, price):
        self.id = Book.couter
        self.name = name
        self.author = author
        self.price = price
        Book.couter = Book.couter + 1

    def __str__(self) -> str:
        return f"{self.id}.) Name: {self.name} Author: {self.author} Price: {self.price}"
