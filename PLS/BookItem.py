from Book import Book

class BookItem(Book):
    def __init__(self, book):
        #self.book = book
        Book.__init__(self, book.author, book.country, book.imageLink, book.language, book.link, book.pages, book.title, book.ISBN, book.year)