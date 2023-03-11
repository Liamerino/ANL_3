from Catalog import Catalog
from BookItem import BookItem
from Book import Book
class Library:
    def __init__(self):
        self.catalog = Catalog()
        self.members = []
        self.bookItems = []
    
    def addBookItem(self, book):
        if isinstance(book, Book):
            bookToAdd = BookItem(book)
            if bookToAdd not in self.bookItems:
                self.bookItems.extend([bookToAdd] * 5)
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
    