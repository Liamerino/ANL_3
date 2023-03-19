from Catalog import Catalog
from BookItem import BookItem
from Book import Book

class Library:
    def __init__(self):
        self.catalog = Catalog()
        self.members = []
        self.bookItems = []
    
    def addBookItem(self, *books):
        for book in books:
            if isinstance(book, Book):
                bookToAdd = BookItem(book)
                if bookToAdd not in self.bookItems:
                    self.bookItems.extend([bookToAdd] * 5)
                    self.catalog.add_book(book)
                    print(f'Five copies of [{book}] have been added to the library')
                else:
                    self.bookItems.append(bookToAdd)
                    print(f'A copy of [{book}] has been added to the library')
            else:
                print(f"[{book}] is not a book and therefore can't be added")
        

    def deleteBookItem(self, bookItem):
        if isinstance(bookItem, BookItem):
            if bookItem in self.bookItems:
                self.bookItems.remove(bookItem)
                print(f'A copy of [{bookItem}] has been deleted')
            else:
                print(f"There are no copies of [{bookItem}] in the library and therefore it can't be deleted")
        else:
            print(f"[{bookItem}] is not a book and therefore it can't be deleted")
    
    def search_book_by_title(self, title):
        copies = 0
        for b in self.bookItems:
            if b.title == title:
                copies += 1
                book = b
        if copies > 0:
            print(f"There are {copies} copies of [{book}] in the library")
            return b
        else:
            print(f"No books with title: {title} were found in the library")
    
    def search_book_by_ISBN(self, isbn):
        copies = 0
        for b in self.bookItems:
            if b.ISBN == isbn:
                copies += 1
                book = b
        if copies > 0:
            print(f"There are {copies} copies of [{book}] in the library")
            return b
        else:
            print(f"No books with ISBN: {isbn} were found in the library")