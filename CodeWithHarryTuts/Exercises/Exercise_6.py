class Library:
    def __init__(self, no_of_books):
        self.no_of_books = no_of_books
        self.books = []

    def check(self):
        if len(self.books) == self.no_of_books:
            return True

    def showBooks(self):
        print(self.books)
        print(self.no_of_books)
    def addBooks(self, book):
        self.books.append(book)
        self.no_of_books+=1

    def removeBooks(self, book):
        if (book not in self.books):
            print("Book not found")
        else:
            ind = self.books.index(book)
            self.books.pop(ind)
            self.no_of_books-=1

lib1 = Library(5)
lib1.addBooks("AA")
lib1.showBooks()
print(lib1.check())

lib1.addBooks("FF")
lib1.showBooks()
print(lib1.check())


lib1.removeBooks("BB")
lib1.showBooks()
print(lib1.check())




