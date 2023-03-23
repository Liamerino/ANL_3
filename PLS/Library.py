from Settings import  buttons, colors, clear
from Catalog import Catalog
from BookItem import BookItem
from Book import Book
from Person import Person
from Member import Member
import csv
import json
import os

class Library:
    def __init__(self):
        self.catalog = Catalog()
        self.members : list[Person] = []     #defining types does nothing at runtime, but while wrinting it helps with autocomplete
        self.bookItems : list[BookItem] = []
        

    #####################################
    # MEMBERS
    #####################################
    def load_members(self, path):
        if not os.getcwd() in os.path.abspath(path):
            print("cant load, file not the correct directory")
            return
        
        with open(path, 'r') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=';')
            firstline = True
            for row in csv_reader:
                if firstline:
                    #print(f'Column names are {", ".join(row)}')
                    firstline = False
                else:
                   if len(row) == 10:
                    self.add_member(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9])
                    print(f"loading user:{row[0]} {row[7]}")
            print(f'loading users done.')

    def add_member(self, number, givenName, surname,streetAddress, zipCode, city, emailAddress, username, password, telephoneNumber):
        for p in self.members:
            if p.username == username:
                return
        self.members.append(
                Member(self, number,givenName, surname,streetAddress, zipCode, city, emailAddress, username, password, telephoneNumber)
        )







    #####################################
    # BOOKS
    #####################################
    def load_books(self, path):
        with open(path, 'r') as f:
            books = json.load(f)
            for book in books:
                bookToAdd = Book(book["author"], book["country"],book["imageLink"], book["language"], book["link"], book["pages"],book["title"],book["ISBN"], book["year"])
                bookItemToAdd = BookItem(bookToAdd)
                if bookToAdd not in self.bookItems:
                    self.add_book_item(bookItemToAdd,bookItemToAdd,bookItemToAdd,bookItemToAdd,bookItemToAdd)
                else:
                    self.add_book_item(bookItemToAdd)

                if bookToAdd not in self.catalog.books:
                    self.catalog.add_book(bookToAdd)

    def add_book_item(self, *books):
        for book in books:
            if isinstance(book, BookItem):
                self.bookItems.append(book)


    def delete_book_item(self, bookItem):
        if isinstance(bookItem, BookItem):
            if bookItem in self.bookItems:
                self.bookItems.remove(bookItem)
                print(f'A copy of [{bookItem}] has been deleted')
            else:
                print(f"There are no copies of [{bookItem}] in the library and therefore it can't be deleted")
        else:
            print(f"[{bookItem}] is not a book and therefore it can't be deleted")
    
    #search book by: "author" || "title" || "all"
    def search_books_by(self, by,  term):
        sortBy = by.lower()
        termLow = term.lower()
        books : list[BookItem] = [] #type declaration does not effect run time but helps while writing
        for b in self.bookItems:
            if (sortBy == "title" and termLow in b.title.lower() 
                or sortBy == "author" and termLow in b.author.lower()
                or sortBy == "all" and (termLow in b.author.lower() or termLow in b.title.lower())
                ):
                books.append(b)
        return books
    

    def run(self, message = f"{colors.YELLOW} Log in"):
        clear() #clearing console to make it better to shee where the i
        print(f"{message}{colors.WHITE}")
        print(f"====================")
        print(f"Enter username")
        print(f"{colors.GRAY}or enter {colors.RED}[{buttons.goBack}]{colors.GRAY} to shut down the program{colors.WHITE}")
        un = input()
        if un.upper() == buttons.goBack:
            exit()
        if un == "":
            self.run(f"{colors.RED}You cant enter nothing")
            return
        clear() #clearing console to make it better to shee where the i
        print(f"{colors.YELLOW}{un}{colors.WHITE}")
        print(f"====================")
        print(f"Enter password")
        print(f"{colors.GRAY}or nothing to change the username{colors.WHITE}")
        pw = input()

        if pw == "":
            self.run()
            return
        for user in self.members:
            if user.username.upper() == un.upper() and user.password == pw:
                user.start()
                return
        self.run(f"{colors.RED}Wrong username or password")

    def amount_of_copies(self, book):
        if isinstance(book, Book):
            count = 0
            for b in self.bookItems:
                if book.ISBN == b.ISBN: 
                    count += 1
            return count
        else: 
            return 0