from Book import Book

class Catalog:

    def __init__(self):
        self.books = []

    def add_book(self, book):
        if isinstance(book, Book):
            self.books.append(book)
    
    def show_books(self):
        index = 1
        for b in self.books:
            print( f"[{index}] {b}" )
            index += 1

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


    def edit_book(self, book, item, newValue):
        if isinstance(book, Book) and book in self.books:
            if item == "1":
                book.author = newValue
            elif item == "2":
                book.country = newValue
            elif item == "3":
                book.imageLink = newValue
            elif item == "4":
                book.language = newValue
            elif item == "5":
                book.link = newValue
            elif item == "6":
                book.pages = newValue
            elif item == "7":
                book.title = newValue
            elif item == "8":
                book.ISBN = newValue
            elif item == "9":
                book.year = newValue
            

