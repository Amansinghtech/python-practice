from Book import Book
# myLongList = [12, 134, 54, 65, 13435, 2, 62,
#               5, 1, 62452, 16, 45, 13, 422, 36, 14, 6]

# def squaredNumbers():
#     for number in myLongList:
#         yield number ** 2


# mySquares = [x for x in squaredNumbers()]
# print(mySquares)

book1 = Book("Harry Potter", "J.K. Rowling", 999)

for value in book1:
    print(value)
