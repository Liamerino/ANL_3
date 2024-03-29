from Book import Book

class Catalog:

    def __init__(self):
        #defining types does nothing at runtime, but while wrinting it helps with autocomplete
        self.books : list[Book] = []

    def add_book(self, book):
        if isinstance(book, Book):
            self.books.append(book)

    def remove_book(self, book):
        if isinstance(book, Book) and book in self.books:
            self.books.remove(book)

    #search book by: "author" || "title" || "all"
    def search_books_by(self, by, term):
        sortBy = by.lower()
        termLow = term.lower()
        found : list[Book] = [] #type declaration does not effect run time but helps while writing
        for b in self.books:
            if (sortBy == "title" and termLow in b.title.lower() 
                or sortBy == "author" and termLow in b.author.lower()
                or sortBy == "all" and (termLow in b.author.lower() or termLow in b.title.lower())
                ):
                found.append(b)
        return found
