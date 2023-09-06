from Book import Book

INVENTORY = []


# book1 = Book("Harry Potter", "J.K. Rowling", 999)
# book2 = Book("Rich Dad Poor Dad", "Warren Buffet", 1299)

def addBook():
    name = input("Book name: ")
    author = input("Author name: ")
    price = float(input("Price: "))
    book = Book(name, author, price)
    INVENTORY.append(book)


def listBooks():
    for book in INVENTORY:
        print(book)


def main():
    while True:
        print("Choose An Option")
        print("1. Add a new Book")
        print("2. Delete a Book")
        print("3. List all Books")
        print("4. Exit Program")

        choice = int(input("Enter your selection: "))

        if choice == 1:
            addBook()
        if choice == 2:
            pass
        if choice == 3:
            listBooks()
        if choice == 4:
            break

        print("\n----------------------\n")
