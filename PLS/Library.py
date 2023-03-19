from Settings import  colors, clear
from Catalog import Catalog
from BookItem import BookItem
from Book import Book
from Person import Person

class Library:
    def __init__(self):
        self.catalog = Catalog()
        self.persons : list[Person] = []     #defining types does nothing at runtime, but while wrinting it helps with autocomplete
        self.bookItems : list[BookItem] = []

    def add_book_item(self, *books):
        for book in books:
            if isinstance(book, Book):
                bookToAdd = BookItem(book)
                if bookToAdd not in self.bookItems:
                    self.bookItems.extend([bookToAdd] * 5)
                    self.catalog.add_book(book)
                    #print(f'Five copies of [{book}] have been added to the library')
                else:
                    self.bookItems.append(bookToAdd)
                    #print(f'A copy of [{book}] has been added to the library')
            else:
                pass
                #print(f"[{book}] is not a book and therefore can't be added")


    def delete_book_item(self, bookItem):
        if isinstance(bookItem, BookItem):
            if bookItem in self.bookItems:
                self.bookItems.remove(bookItem)
                print(f'A copy of [{bookItem}] has been deleted')
            else:
                print(f"There are no copies of [{bookItem}] in the library and therefore it can't be deleted")
        else:
            print(f"[{bookItem}] is not a book and therefore it can't be deleted")
    
    #search book by: "author" || "title" || "isbn" || "all"
    def search_books_by(self, by,  term):
        sortBy = by.lower()
        books : list[BookItem] = [] #type declaration does not effect run time but helps while writing
        for b in self.bookItems:
            if (sortBy == "title" and term.lower() in b.title.lower() 
                or sortBy == "ibsn" and term in b.ISBN == term 
                or sortBy == "author" and term.lower() in b.author == term.lower()):
                books.append(b)
        return books
    
    

    """
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
    """

    def run(self, message = f"{colors.YELLOW} Log in"):
        clear() #clearing console to make it better to shee where the i
        print(f"{message}{colors.WHITE}")
        print(f"====================")
        print(f"Enter username:")
        un = input()
        if un == "":
            self.run(f"{colors.RED}You cant enter nothing")
            return
        clear() #clearing console to make it better to shee where the i
        print(f"{colors.YELLOW}{un}{colors.WHITE}")
        print(f"====================")
        print(f"Enter password {colors.GRAY}or nothing to change the username{colors.WHITE}:")
        pw = input()

        if pw == "":
            self.run()
            return
        for user in self.persons:
            if user.username.upper() == un.upper() and user.password == pw:
                user.start()
                return
        self.run(f"{colors.RED}Wrong username or password")
    
    def add_person(self, *person):
        for p in person:
            if isinstance(p, Person):
                self.persons.append(p)


