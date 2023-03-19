from colorama import Fore
from Settings import goBack, clear
from Catalog import Catalog
from BookItem import BookItem
from Book import Book
from Person import Person

class Library:
    def __init__(self):
        self.catalog = Catalog()
        self.persons : list[Person] = []     #defining types does nothing at runtime, but while wrinting it helps with autocomplete
        self.bookItems : list[BookItem] = []
    
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

    def run(self, message = f"{Fore.YELLOW}Log in"):
        clear() #clearing console to make it better to shee where the i
        print(f"{message}{Fore.RESET}")
        print(f"====================")
        print(f"Enter username:")
        un = input().upper()
        clear() #clearing console to make it better to shee where the i
        print(f"{Fore.YELLOW}{un}{Fore.RESET}")
        print(f"====================")
        print(f"Enter password {Fore.BLACK}or nothing to change the username{Fore.RESET}:")
        pw = input()

        if pw == "" or un == "":
            self.run()
        for user in self.persons:
            if user.username.upper() == un and user.password == pw:
                user.start()
                return
        self.run(f"{Fore.RED}Wrong username or password")
    
    def add_person(self, *person):
        for p in person:
            if isinstance(p, Person):
                self.persons.append(p)


