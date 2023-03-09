from Book import Book

class Catalog:

    def __init__(self):
        self.books = []

    def add_book(self, book):
        if not isinstance(book, Book):
            print(f"[{book}] isnt a book therefore cant be added to the catalog.")
        elif book in self.books:
            print(f"[{book.title}] is already in the catalog")
        else:
            print(f"[{book.title}] has been added to the catalog")
            self.books.append(book)
    
    def show_books(self):
        index = 1
        for b in self.books:
            print( f"[{index}] {b}" )
            index += 1

    def remove_book(self, book):
        if not isinstance(book, Book):
            print(f"[{book}] isnt a book therefore cant be removed from the catalog.")
        elif book not in self.books: 
            print(f"[{book.title}] is not in the catalog")
        else:
            print(f"[{book.title}] has been removed from the catalog")
            self.books.remove(book)

    def search_book_by_title(self,title):
        for b in self.books:
            if b.title == title:
                return b